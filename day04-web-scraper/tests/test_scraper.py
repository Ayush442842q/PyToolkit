import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from scraper import parse_headlines, display_headlines

def test_parse_headlines_empty():
    result = parse_headlines(None)
    assert result == []
    print("✅ test_parse_headlines_empty passed!")

test_parse_headlines_empty()