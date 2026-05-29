"""
Fahrenheit to Celsius Converter.
Takes a temperature in Fahrenheit and converts it to Celsius.
"""


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert a temperature from Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    """Get Fahrenheit input from user and display Celsius equivalent."""
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:.1f}°F is equal to {celsius:.2f}°C")


if __name__ == '__main__':
    main()
