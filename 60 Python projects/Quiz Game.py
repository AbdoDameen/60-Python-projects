def check_guess(guess: str, answer: str) -> bool:
    """
    Check the user's guess against the correct answer.
    Gives up to 2 retries on wrong answers.

    Args:
        guess: The player's initial guess.
        answer: The correct answer.

    Returns:
        True if the player got it right, False otherwise.
    """
    global score
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score += 1
            return True
        else:
            attempts += 1
            if attempts < max_attempts:
                guess = input("Sorry, wrong answer. Try again: ")
            else:
                print(f"The correct answer is {answer}")

    return False


def main():
    """Run a simple animal guessing quiz game."""
    global score
    score = 0

    print("Guess the Animal")

    guess1 = input("Which bear lives at the North Pole? ")
    check_guess(guess1, "Polar Bear")

    guess2 = input("What is the fastest land animal? ")
    check_guess(guess2, "Cheetah")

    guess3 = input("What is the largest animal? ")
    check_guess(guess3, "Blue Whale")

    print(f"Your score is {score}")


if __name__ == '__main__':
    main()
