import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from sender import is_valid_email, create_message

def test_valid_email():
    assert is_valid_email("test@gmail.com") == True
    assert is_valid_email("ayush@yahoo.com") == True
    print("✅ test_valid_email passed!")

test_valid_email()
