import random


def main():
    """Play Rock, Paper, Scissors against the computer until the player types 'End'."""
    choices = ['Rock', 'Paper', 'Scissors']
    cpu_score = 0
    player_score = 0

    while True:
        # Computer makes a fresh random choice each round
        computer = random.choice(choices)

        player = input("Rock, Paper or Scissors? (type 'End' to quit): ").capitalize()

        # Check for exit condition first
        if player == "End":
            print("Final Scores:")
            print(f"CPU: {cpu_score}")
            print(f"Player: {player_score}")
            break

        # Validate input
        if player not in choices:
            print("Invalid choice. Please pick Rock, Paper, or Scissors.")
            continue

        # Determine the outcome
        if player == computer:
            print('Tie')
        elif player == "Rock":
            if computer == 'Paper':
                print(f"You lose! {computer} covers {player}")
                cpu_score += 1
            else:
                print(f"You win! {player} smashes {computer}")
                player_score += 1
        elif player == "Paper":
            if computer == "Scissors":
                print(f"You lose! {computer} cuts {player}")
                cpu_score += 1
            else:
                print(f"You win! {player} covers {computer}")
                player_score += 1
        elif player == "Scissors":
            if computer == "Rock":
                print(f"You lose! {computer} smashes {player}")
                cpu_score += 1
            else:
                print(f"You win! {player} cuts {computer}")
                player_score += 1


if __name__ == '__main__':
    main()
