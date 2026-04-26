import sys
import os
import shutil
sys.path.insert(0, os.path.abspath(".."))

from qr_generator import get_qr_info, _detect_data_type, ensure_output_folder

def test_detect_url():
    assert _detect_data_type("https://github.com") == "URL"
    print("✅ test_detect_url passed!")

test_detect_url()

def test_detect_plain_text():
    assert _detect_data_type("Hello World") == "Plain Text"
    print("✅ test_detect_plain_text passed!")

test_detect_plain_text()

def test_detect_email():
    assert _detect_data_type("user@example.com") == "Email Address"
    print("✅ test_detect_email passed!")

test_detect_email()

def test_get_qr_info():
    info = get_qr_info("https://github.com")
    assert info["type"] == "URL"
    assert info["length"] == len("https://github.com")
    print("✅ test_get_qr_info passed!")

test_get_qr_info()

def test_ensure_output_folder():
    test_folder = "test_qr_temp"
    ensure_output_folder(test_folder)
    assert os.path.exists(test_folder)
    shutil.rmtree(test_folder)
    print("✅ test_ensure_output_folder passed!")

test_ensure_output_folder()
