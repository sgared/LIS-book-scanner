#!/usr/bin/env python3
"""
LIS Book Scanner - Main Entry Point for Replit
Simplified launcher that handles setup and runs the Flask app
"""

import os
import sys
import subprocess

def setup_and_run():
    """Setup environment and run the Flask application"""
    print("🚀 Starting LIS Book Scanner on Replit...")
    
    # Change to server-side directory
    server_dir = os.path.join(os.path.dirname(__file__), 'server-side')
    if os.path.exists(server_dir):
        os.chdir(server_dir)
        print(f"📁 Changed to directory: {os.getcwd()}")
    
    # Check if we can import the required modules
    try:
        import flask
        print("✅ Flask is available")
    except ImportError:
        print("❌ Flask not found, attempting to install...")
        subprocess.run([sys.executable, "-m", "pip", "install", "flask"])
    
    try:
        import PIL
        print("✅ PIL is available")
    except ImportError:
        print("❌ PIL not found, attempting to install...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pillow"])
    
    # Try to run the main app
    try:
        print("🌟 Importing and starting Flask app...")
        from app_production import app
        
        # Run with Replit-friendly settings
        print("🌐 Starting Flask server on 0.0.0.0:5000...")
        app.run(host='0.0.0.0', port=5000, debug=True)
        
    except ImportError as e:
        print(f"❌ Failed to import app: {e}")
        print("🔄 Trying direct execution...")
        
        # Fallback: execute the file directly
        subprocess.run([sys.executable, "app_production.py"])

if __name__ == "__main__":
    setup_and_run()