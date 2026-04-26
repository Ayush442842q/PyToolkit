import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from qr_generator import get_qr_info, _detect_data_type, ensure_output_folder

def test_detect_url():
    assert _detect_data_type("https://github.com") == "URL"
    assert _detect_data_type("http://example.com") == "URL"
    print("✅ test_detect_url passed!")

test_detect_url()
