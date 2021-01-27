def check_guess(guess, answer):
    global score
    still_guessing=True
    attempt=0
    while still_guessing and attempt <3:
        if guess.lower()==answer.lower():
            print("Correct Answer")
            score=score+1
            still_guessing=False
        else:
            if attempt<2:
                guess=input("Sorry Wrong Answer, try again")
            attempt=attempt+1
    if attempt == 3:
        print("The Correct answer is ",answer )

score=0
print("Guess the Animal")
guess1=input("which bear lives at the North Pole? ")
check_guess(guess1, "Polar Bear")
guess2=input("What is the Fastest Land Animal? ")
check_guess(guess2, "Cheetah")
guess3=input("What is the Largest Animal? ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+str(score))
