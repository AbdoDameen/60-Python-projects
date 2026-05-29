"""
BMI Calculator.
Takes height (cm) and weight (kg) input from the user and calculates BMI.
"""


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """
    Calculate Body Mass Index from height in centimeters and weight in kilograms.
    Returns the BMI value.
    """
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight_kg / (height_m * height_m)
    return bmi


def classify_bmi(bmi: float) -> str:
    """Return a weight classification string based on BMI value."""
    if bmi <= 0:
        return "invalid"
    elif bmi <= 16:
        return "severely underweight"
    elif bmi <= 18.5:
        return "underweight"
    elif bmi <= 25:
        return "healthy"
    elif bmi <= 30:
        return "overweight"
    else:
        return "severely overweight"


def main():
    """Get user input, calculate BMI, and display results."""
    try:
        height_cm = float(input("Enter your height in centimeters: "))
        weight_kg = float(input("Enter your weight in kg: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if height_cm <= 0 or weight_kg <= 0:
        print("Height and weight must be positive numbers.")
        return

    bmi = calculate_bmi(height_cm, weight_kg)
    classification = classify_bmi(bmi)

    print(f"Your Body Mass Index is: {bmi:.2f}")
    if classification == "invalid":
        print("Enter valid details.")
    else:
        print(f"You are {classification}.")


if __name__ == '__main__':
    main()
