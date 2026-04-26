import sys
import os
import shutil
sys.path.insert(0, os.path.abspath(".."))

from downloader import is_valid_url, ensure_download_folder, display_info

def test_valid_url():
    assert is_valid_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == True
    print("✅ test_valid_url passed!")

test_valid_url()

def test_invalid_url():
    assert is_valid_url("not-a-url") == False
    assert is_valid_url("") == False
    print("✅ test_invalid_url passed!")

test_invalid_url()

def test_ensure_download_folder():
    test_folder = "test_downloads_temp"
    ensure_download_folder(test_folder)
    assert os.path.exists(test_folder)
    shutil.rmtree(test_folder)
    print("✅ test_ensure_download_folder passed!")

test_ensure_download_folder()

def test_display_info_none():
    result = display_info(None)
    assert result is None
    print("✅ test_display_info_none passed!")

test_display_info_none()
