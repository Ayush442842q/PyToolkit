import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from downloader import is_valid_url, ensure_download_folder

def test_valid_url():
    assert is_valid_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == True
    print("✅ test_valid_url passed!")

test_valid_url()
