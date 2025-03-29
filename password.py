import random
import string

def generate_strong_password(length=12):
    """
    Generate a strong password with the specified length (default: 12).
    The password will include uppercase letters, lowercase letters, numbers, and symbols.

    Args:
        length (int): The desired length of the password (must be between 12 and 16).

    Returns:
        str: The generated password.
    """
    if length < 12 or length > 16:
        raise ValueError("Password length must be between 12 and 16 characters.")
    
    # Define character pools
    letters = string.ascii_letters  # Uppercase and lowercase letters
    digits = string.digits  # Numbers
    symbols = string.punctuation  # Special characters
    
    # Ensure at least one character from each pool
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random choices from all pools
    all_characters = letters + digits + symbols
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the password list to avoid predictable p
    #test
