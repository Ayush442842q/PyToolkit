import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from scraper import parse_headlines, display_headlines

def test_parse_headlines_empty():
    result = parse_headlines(None)
    assert result == []
    print("✅ test_parse_headlines_empty passed!")

test_parse_headlines_empty()

def test_parse_headlines_returns_list():
    result = parse_headlines(None)
    assert isinstance(result, list)
    print("✅ test_parse_headlines_returns_list passed!")

test_parse_headlines_returns_list()

def test_display_headlines_empty():
    result = display_headlines([])
    assert result is None
    print("✅ test_display_headlines_empty passed!")

test_display_headlines_empty()