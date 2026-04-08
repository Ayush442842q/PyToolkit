import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from generator import generate_password, validate_length, check_password_strength

def test_password_length():
    password = generate_password(12)
    assert len(password) == 12
    print("✅ test_password_length passed!")

test_password_length()
def test_password_has_digits():
    password = generate_password(12, use_digits=True, use_symbols=False)
    has_digit = any(c.isdigit() for c in password)
    assert has_digit == True
    print("✅ test_password_has_digits passed!")

test_password_has_digits()