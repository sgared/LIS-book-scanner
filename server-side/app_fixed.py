from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for
import os, cv2, pytesseract, easyocr, spacy, nltk, pandas as pd, requests, sqlite3
from datetime import datetime
from werkzeug.utils import secure_filename
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend
import io, base64
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Load models
nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)

# Load spaCy model with error handling
try:
    nlp = spacy.load("en_core_web_sm")
    print("✓ spaCy English model loaded successfully")
except OSError:
    print("⚠ Warning: spaCy English model not found. Please install it:")
    print("  python -m spacy download en_core_web_sm")
    nlp = None

reader = easyocr.Reader(["en"], gpu=False)

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCRProcessor:
    def __init__(self):
        self.reader = easyocr.Reader(["en"], gpu=False)
        self.init_database()

    def init_database(self):
        """Initialize SQLite database for catalog storage"""
        conn = sqlite3.connect('catalog.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id TEXT UNIQUE,
                title TEXT,
                author TEXT,
                year TEXT,
                isbn TEXT,
                publisher TEXT,
                keywords TEXT,
                enriched TEXT,
                full_text TEXT,
                cover_path TEXT,
                timestamp TEXT,
                confidence REAL
            )
        ''')
        conn.commit()
        conn.close()

    def preprocess_image(self, image_path):
        """Enhanced image preprocessing with noise reduction"""
        img = cv2.imread(image_path)
        if img is None:
            return None
            
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Noise reduction
        denoised = cv2.fastNlMeansDenoising(gray)
        
        # Adaptive thresholding
        thresh = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                     cv2.THRESH_BINARY, 11, 2)
        
        # Morphological operations to clean up
        kernel = np.ones((1,1), np.uint8)
        processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        return processed

    def process_book_image(self, image_path):
        """Process a single book image with dual OCR engines"""
        # Preprocess image
        processed_img = self.preprocess_image(image_path)
        
        if processed_img is None:
            return "Error: Could not process image"
        
        # Try Tesseract first
        try:
            tesseract_text = pytesseract.image_to_string(processed_img, config='--psm 6')
        except:
            tesseract_text = ""
        
        # Try EasyOCR if Tesseract fails or produces little text
        easyocr_text = ""
        if len(tesseract_text.strip()) < 50:
            try:
                results = self.reader.readtext(processed_img, detail=0, paragraph=True)
                easyocr_text = " ".join(results)
            except:
                easyocr_text = ""
        
        # Use the better result
        if len(easyocr_text) > len(tesseract_text):
            return easyocr_text
        else:
            return tesseract_text

    def save_to_database(self, metadata, full_text):
        """Save extracted metadata to database"""
        conn = sqlite3.connect('catalog.db')
        c = conn.cursor()
        
        try:
            c.execute('''
                INSERT OR REPLACE INTO books 
                (book_id, title, author, year, isbn, publisher, keywords, 
                 enriched, full_text, cover_path, timestamp, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                metadata.get("book_id", ""), metadata.get("title", ""),
                metadata.get("author", ""), metadata.get("year", ""),
                metadata.get("isbn", ""), metadata.get("publisher", ""),
                metadata.get("keywords", ""), metadata.get("enriched", ""),
                full_text, metadata.get("cover_path", ""),
                datetime.now().isoformat(), 0.95
            ))
            conn.commit()
        except Exception as e:
            print(f"Database save error: {e}")
        finally:
            conn.close()


def enhanced_extract_metadata(full_text, image_path):
    """Extract comprehensive metadata using multiple techniques from notebook"""
    import re
    
    # Basic regex extraction
    title = "Unknown Title"
    author = "Unknown Author"
    year = "Unknown"
    isbn = None
    publisher = "Unknown"
    
    # Enhanced title extraction from first meaningful line
    lines = full_text.split('\\n')
    for line in lines[:5]:  # Check first 5 lines
        line = line.strip()
        if len(line) > 10 and not line.isdigit():
            title = line
            break
    
    # Extract publication year with multiple patterns
    year_patterns = [
        r'\\b(19|20)\\d{2}\\b',
        r'Copyright.*?(19|20)\\d{2}',
        r'©.*?(19|20)\\d{2}'
    ]
    for pattern in year_patterns:
        year_match = re.search(pattern, full_text)
        if year_match:
            year = re.search(r'(19|20)\\d{2}', year_match.group(0)).group(0)
            break
    
    # Extract ISBN with enhanced pattern
    isbn_match = re.search(
        r"(978|979)[- ]?\\d{1,5}[- ]?\\d{1,7}[- ]?\\d{1,7}[- ]?\\d", full_text
    )
    if isbn_match:
        isbn = isbn_match.group(0).replace(" ", "").replace("-", "")

    # Use spaCy for named entity recognition (if available)
    if nlp:
        try:
            doc = nlp(full_text[:100000])  # Limit text length for performance
            persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
            if persons and author == "Unknown Author":
                author = persons[0]
        except Exception as e:
            print(f"spaCy processing error: {e}")

    # Extract keywords using NLTK
    words = nltk.word_tokenize(full_text.lower())
    words = [w for w in words if w.isalpha() and len(w) > 4]
    freq = nltk.FreqDist(words)
    keywords = ", ".join([w for w, c in freq.most_common(8)])

    # Open Library API enrichment
    enriched = False
    if isbn and len(isbn) >= 10:
        try:
            url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
            resp = requests.get(url, timeout=10)
            data = resp.json()
            key = f"ISBN:{isbn}"
            if key in data:
                ol = data[key]
                title = ol.get("title", title)
                if "authors" in ol:
                    author = ol["authors"][0]["name"]
                if "publish_date" in ol:
                    year = ol["publish_date"][-4:]
                publisher = ol.get("publishers", [{}])[0].get("name", publisher)
                enriched = True
        except:
            pass

    return {
        "book_id": f"book_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn or "N/A",
        "publisher": publisher,
        "keywords": keywords,
        "enriched": "Yes (Open Library)" if enriched else "No",
        "cover_path": image_path
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('files')
        results = []
        
        for file in files:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            
            # Enhanced OCR processing
            processor = OCRProcessor()
            full_text = processor.process_book_image(path)
            meta = enhanced_extract_metadata(full_text, path)
            
            # Add image data for display
            with open(path, 'rb') as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
                meta["image"] = f"data:image/jpeg;base64,{img_data}"
            
            results.append(meta)
            
            # Save to database
            processor.save_to_database(meta, full_text)
        
        return render_template('results.html', results=results)
    
    return render_template('index.html')


@app.route('/analytics')
def analytics():
    """Analytics dashboard with visualizations"""
    try:
        # Get data from database
        conn = sqlite3.connect('catalog.db')
        df = pd.read_sql("SELECT * FROM books", conn)
        conn.close()
        
        if len(df) == 0:
            return render_template('analytics.html', 
                                 total_books=0, 
                                 enriched_books=0, 
                                 visualizations=None)
        
        # Generate visualizations
        visualizations = create_visualizations(df)
        
        # Calculate statistics
        stats = {
            'total_books': len(df),
            'enriched_books': len(df[df['enriched'].str.contains('Yes', na=False)]),
            'unique_authors': len(df['author'].unique()),
            'avg_year': int(pd.to_numeric(df['year'], errors='coerce').mean()) if len(df) > 0 else 'N/A'
        }
        
        return render_template('analytics.html', 
                             total_books=stats['total_books'],
                             enriched_books=stats['enriched_books'],
                             unique_authors=stats['unique_authors'],
                             avg_year=stats['avg_year'],
                             visualizations=visualizations)
    except Exception as e:
        return f"Error generating analytics: {str(e)}", 500


@app.route('/database')
def database_view():
    """Database management interface"""
    try:
        conn = sqlite3.connect('catalog.db')
        df = pd.read_sql("SELECT * FROM books ORDER BY timestamp DESC", conn)
        conn.close()
        
        # Convert DataFrame to list of dictionaries for template
        records = df.to_dict('records')
        
        return render_template('database.html', records=records, total=len(records))
    except Exception as e:
        return f"Database error: {str(e)}", 500


def create_visualizations(df):
    """Create data visualizations from the notebook"""
    visualizations = {}
    
    try:
        # Publication year distribution
        plt.figure(figsize=(10, 6))
        years = pd.to_numeric(df['year'], errors='coerce').dropna()
        if len(years) > 0:
            plt.hist(years, bins=20, alpha=0.7, color='#1a5f3f', edgecolor='black')
            plt.title('Publication Year Distribution')
            plt.xlabel('Year')
            plt.ylabel('Count')
            plt.grid(True, alpha=0.3)
            
            img_buffer = io.BytesIO()
            plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
            img_buffer.seek(0)
            year_chart = base64.b64encode(img_buffer.getvalue()).decode()
            visualizations['year_distribution'] = year_chart
            plt.close()
        
        # Enrichment status pie chart
        plt.figure(figsize=(8, 8))
        enriched_counts = df['enriched'].value_counts()
        if len(enriched_counts) > 0:
            colors = ['#1a5f3f', '#d32f2f']
            plt.pie(enriched_counts.values, labels=enriched_counts.index, 
                   autopct='%1.1f%%', colors=colors, startangle=90)
            plt.title('API Enrichment Status')
            
            img_buffer = io.BytesIO()
            plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
            img_buffer.seek(0)
            enrichment_chart = base64.b64encode(img_buffer.getvalue()).decode()
            visualizations['enrichment_status'] = enrichment_chart
            plt.close()
        
        # Keywords word cloud
        all_keywords = ' '.join(df['keywords'].fillna('').astype(str))
        if len(all_keywords.strip()) > 0:
            wordcloud = WordCloud(width=800, height=400, 
                                background_color='white',
                                colormap='Greens').generate(all_keywords)
            
            plt.figure(figsize=(12, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('Most Common Keywords')
            
            img_buffer = io.BytesIO()
            plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
            img_buffer.seek(0)
            wordcloud_chart = base64.b64encode(img_buffer.getvalue()).decode()
            visualizations['wordcloud'] = wordcloud_chart
            plt.close()
            
    except Exception as e:
        print(f"Visualization error: {e}")
    
    return visualizations


@app.route('/download/<format>')
def download(format):
    """Enhanced download with multiple formats"""
    try:
        conn = sqlite3.connect('catalog.db')
        df = pd.read_sql("SELECT * FROM books", conn)
        conn.close()
        
        if format == 'csv':
            csv_data = df.to_csv(index=False)
            return send_file(
                io.BytesIO(csv_data.encode()),
                mimetype='text/csv',
                as_attachment=True,
                download_name=f'catalog_{datetime.now().strftime("%Y%m%d")}.csv'
            )
        elif format == 'json':
            json_data = df.to_json(orient='records', indent=2)
            return send_file(
                io.BytesIO(json_data.encode()),
                mimetype='application/json',
                as_attachment=True,
                download_name=f'catalog_{datetime.now().strftime("%Y%m%d")}.json'
            )
        else:
            return "Format not supported. Available: csv, json", 400
    except Exception as e:
        return f"Download error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)