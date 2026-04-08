import random
import string

# Character sets
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """Generates a random password with given options."""
    characters = LOWERCASE

    if use_upper:
        characters += UPPERCASE
    if use_digits:
        characters += DIGITS
    if use_symbols:
        characters += SYMBOLS

    password = "".join(random.choice(characters) for _ in range(length))
    return password