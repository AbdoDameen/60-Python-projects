"""
Roman Numerals to Decimal Converter.
Takes a Roman numeral string (e.g., 'XIV') and converts it to a decimal number.
"""

# Mapping of Roman numeral characters to their decimal values
ROMAN_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_numeral_to_decimal(roman_numeral: str) -> int:
    """
    Convert a Roman numeral string to a decimal integer.
    Subtracts when a smaller numeral precedes a larger one (e.g., IV = 4).
    """
    total = 0
    for i in range(len(roman_numeral) - 1):
        left = roman_numeral[i]
        right = roman_numeral[i + 1]
        if ROMAN_VALUES[left] < ROMAN_VALUES[right]:
            total -= ROMAN_VALUES[left]
        else:
            total += ROMAN_VALUES[left]
    total += ROMAN_VALUES[roman_numeral[-1]]
    return total


def main():
    """Get Roman numeral input from user and display decimal equivalent."""
    user_input = input("Enter a Roman numeral (e.g., XIV, MCMXC): ").strip().upper()
    if not user_input:
        print("No input provided.")
        return

    # Validate that all characters are valid Roman numerals
    for char in user_input:
        if char not in ROMAN_VALUES:
            print(f"Invalid Roman numeral character: '{char}'")
            return

    result = roman_numeral_to_decimal(user_input)
    print(f"{user_input} = {result}")


if __name__ == '__main__':
    main()
