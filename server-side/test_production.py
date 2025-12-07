#!/usr/bin/env python3
"""
Simple tests for LIS Book Scanner production version
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'web_app'))

def test_app_import():
    """Test that the production app can be imported"""
    try:
        import app_production
        print("✅ Production app imports successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import production app: {e}")
        return False

def test_flask_app():
    """Test Flask app creation"""
    try:
        from app_production import app
        with app.test_client() as client:
            # Test health endpoint
            response = client.get('/health')
            assert response.status_code == 200, f"Health check failed: {response.status_code}"
            
            # Test main page
            response = client.get('/')
            assert response.status_code == 200, f"Main page failed: {response.status_code}"
            
        print("✅ Flask app works correctly")
        return True
    except Exception as e:
        print(f"❌ Flask app test failed: {e}")
        return False

def test_database():
    """Test database initialization"""
    try:
        from app_production import init_database
        result = init_database()
        assert result == True, "Database initialization failed"
        print("✅ Database initialization successful")
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_metadata_extraction():
    """Test metadata extraction function"""
    try:
        from app_production import extract_metadata
        
        test_text = """
        The Great Gatsby
        By F. Scott Fitzgerald
        Copyright 1925
        ISBN 978-0-7432-7356-5
        Scribner Publishing
        """
        
        result = extract_metadata(test_text, "test.txt")
        
        assert 'title' in result, "Title not extracted"
        assert 'author' in result, "Author not extracted"
        assert result['title'] != 'Unknown Title', "Title extraction failed"
        
        print("✅ Metadata extraction works correctly")
        return True
    except Exception as e:
        print(f"❌ Metadata extraction test failed: {e}")
        return False

def run_tests():
    """Run all tests"""
    tests = [
        test_app_import,
        test_flask_app,
        test_database,
        test_metadata_extraction
    ]
    
    passed = 0
    failed = 0
    
    print("🧪 Running LIS Book Scanner Tests...")
    print("=" * 50)
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            failed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Deployment ready!")
        return 0
    else:
        print("⚠️ Some tests failed. Check the output above.")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)