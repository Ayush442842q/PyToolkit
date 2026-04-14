import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from shortener import is_valid_url, get_history_count, load_history, save_history, clear_history

def test_valid_url_https():
    assert is_valid_url("https://google.com") == True
    print("✅ test_valid_url_https passed!")

test_valid_url_https()

def test_valid_url_http():
    assert is_valid_url("http://example.com") == True
    print("✅ test_valid_url_http passed!")

test_valid_url_http()

def test_invalid_url():
    assert is_valid_url("not-a-url") == False
    assert is_valid_url("www.google.com") == False
    print("✅ test_invalid_url passed!")

test_invalid_url()
