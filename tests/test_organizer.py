import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from organizer import get_file_category, get_files, get_file_count

def test_get_file_category():
    assert get_file_category(".jpg") == "Images"
    assert get_file_category(".mp4") == "Videos"
    assert get_file_category(".pdf") == "Documents"
    assert get_file_category(".xyz") == "Others"
    print("✅ test_get_file_category passed!")

test_get_file_category()


def test_get_file_category_case_insensitive():
    assert get_file_category(".JPG") == "Images"
    assert get_file_category(".MP4") == "Videos"
    assert get_file_category(".PDF") == "Documents"
    print("✅ test_case_insensitive passed!")

test_get_file_category_case_insensitive()