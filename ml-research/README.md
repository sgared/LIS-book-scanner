# 🧠 LIS Book Scanner - ML Research & Training

> **Jupyter notebook environment for machine learning experiments and model training**

## 🎯 Purpose
This folder contains research tools for:
- **OCR algorithm experimentation**
- **NLP model training** 
- **Performance benchmarking**
- **Data analysis and visualization**
- **Ground truth dataset creation**

## 📁 Contents
```
ml-research/
├── LIS_OCR_Project.ipynb     # Main research notebook
├── ground_truth_template.csv # Training data template
└── samples/                  # Test images for experiments
    ├── IMG_4330.jpeg → IMG_4334.jpeg
    └── sample_01.jpg → sample_10.jpg
```

## 🚀 Getting Started

### Prerequisites
```bash
# Install Jupyter and dependencies
pip install jupyter pandas numpy matplotlib opencv-python pillow
pip install tesseract easyocr spacy transformers
```

### Launch Notebook
```bash
# Start Jupyter Lab
jupyter lab

# Or Jupyter Notebook
jupyter notebook

# Open LIS_OCR_Project.ipynb
```

## 🔬 Research Areas

### 1. **OCR Accuracy Analysis**
- Compare Tesseract vs EasyOCR performance
- Test different preprocessing techniques
- Measure confidence scores and accuracy

### 2. **NLP Enhancement** 
- Train custom named entity recognition models
- Improve metadata extraction algorithms
- Develop book-specific text analysis

### 3. **Model Training**
- Fine-tune existing models on book data
- Create custom classification models
- Develop ensemble approaches

### 4. **Benchmark Testing**
- Performance metrics across different book types
- Speed vs accuracy trade-offs
- Resource usage analysis

## 📊 Sample Data
The `samples/` folder contains:
- **Real book images** (IMG_*.jpeg)
- **Test samples** (sample_*.jpg)
- Various book covers and title pages for testing

## 📋 Ground Truth Template
Use `ground_truth_template.csv` to create training datasets:
```csv
filename,title,author,year,isbn,publisher,confidence
sample_01.jpg,Book Title,Author Name,2023,1234567890,Publisher,95
```

## 🧪 Experiment Workflow
1. **Load sample images** from `samples/` directory
2. **Run OCR experiments** with different parameters
3. **Analyze results** and compare accuracy
4. **Document findings** in notebook cells
5. **Export improved models** for production use

## 🔄 Integration
Research results can be integrated into:
- **Client-side app** (`../client-side/`)
- **Server-side app** (`../server-side/`)
- **Production deployments**

## 📈 Expected Outcomes
- Improved OCR accuracy for book scanning
- Better metadata extraction algorithms
- Optimized processing parameters
- Custom trained models for book-specific tasks