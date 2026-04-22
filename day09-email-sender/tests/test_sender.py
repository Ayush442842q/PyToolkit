import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from sender import is_valid_email, create_message, log_email, view_log

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

def test_create_message():
    msg = create_message("sender@gmail.com", "recipient@gmail.com", "Test Subject", "Test Body")
    assert msg["From"] == "sender@gmail.com"
    assert msg["To"] == "recipient@gmail.com"
    assert msg["Subject"] == "Test Subject"
    print("✅ test_create_message passed!")

test_create_message()

def test_log_email():
    log_email("test@gmail.com", "Test Subject", "SUCCESS")
    assert os.path.exists("email_log.txt")
    print("✅ test_log_email passed!")

test_log_email()
