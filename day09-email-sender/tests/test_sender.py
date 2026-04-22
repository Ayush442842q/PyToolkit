import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from sender import is_valid_email, create_message

def test_valid_email():
    assert is_valid_email("test@gmail.com") == True
    assert is_valid_email("ayush@yahoo.com") == True
    print("✅ test_valid_email passed!")

test_valid_email()

def test_invalid_email():
    assert is_valid_email("notanemail") == False
    assert is_valid_email("missing@dot") == False
    assert is_valid_email("") == False
    print("✅ test_invalid_email passed!")

test_invalid_email()
