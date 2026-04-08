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
def validate_length(length):
    """Validates that password length is between 6 and 128."""
    if length < 6:
        print("⚠️ Password too short! Minimum length is 6.")
        return False
    if length > 128:
        print("⚠️ Password too long! Maximum length is 128.")
        return False
    return True
def check_password_strength(password):
    """Returns strength of password: Weak, Medium or Strong."""
    has_upper = any(c in UPPERCASE for c in password)
    has_digit = any(c in DIGITS for c in password)
    has_symbol = any(c in SYMBOLS for c in password)
    length = len(password)

    if length >= 12 and has_upper and has_digit and has_symbol:
        return "💪 Strong"
    elif length >= 8 and (has_upper or has_digit):
        return "👍 Medium"
    else:
        return "⚠️ Weak"
def main():
    """Main function to run the password generator."""
    print("🔐 Password Generator")
    print("-" * 30)

    length = int(input("Enter password length (6-128): "))
    if not validate_length(length):
        return

    use_upper = input("Include uppercase? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_upper, use_digits, use_symbols)
    strength = check_password_strength(password)

    print(f"\n✅ Generated Password: {password}")
    print(f"💡 Strength: {strength}")

if __name__ == "__main__":
    main()