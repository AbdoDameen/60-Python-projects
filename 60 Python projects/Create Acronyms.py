"""
Acronym Creator.
Takes a phrase from the user and creates an acronym from the first letter of each word.
"""


def create_acronym(phrase: str) -> str:
    """
    Convert a phrase into an acronym by taking the first letter of each word
    and converting it to uppercase.
    """
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym


def main():
    """Get a phrase from the user and print its acronym."""
    phrase = input("Enter a phrase: ").strip()
    if not phrase:
        print("No phrase entered.")
        return
    result = create_acronym(phrase)
    print(f"Acronym: {result}")


if __name__ == '__main__':
    main()
