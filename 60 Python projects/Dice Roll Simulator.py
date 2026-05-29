"""Simulate rolling a pair of dice."""

import random

MIN_VALUE = 1
MAX_VALUE = 6

roll_again = "yes"

while roll_again == "yes" or (roll_again and roll_again[0].lower() == "y"):
    print("Rolling the dice...")
    print("The values are:")
    print(random.randint(MIN_VALUE, MAX_VALUE))
    print(random.randint(MIN_VALUE, MAX_VALUE))

    roll_again = input("Roll the dice again? (yes/no) ")

if __name__ == '__main__':
    pass
