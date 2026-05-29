"""Generate a random password of a specified length."""

import random


def generate_password(length: int) -> str:
    """Generate a random password using letters, digits, and special characters."""
    characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    # Use random.choices instead of random.sample to allow repetition
    # and to handle lengths longer than the character set
    password = "".join(random.choices(characters, k=length))
    return password


if __name__ == "__main__":
    try:
        password_length = int(input("Enter the length of the password: "))
        if password_length < 1:
            print("Password length must be at least 1.")
        else:
            print(generate_password(password_length))
    except ValueError:
        print("Error: please enter a valid number.")
