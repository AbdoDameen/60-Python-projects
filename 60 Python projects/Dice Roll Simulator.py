import random
min_val=1
max_val=6

roll_again="yes"

while roll_again=="yes" or roll_again[0].lower()=="y":
    print("Rolling the Dices...")
    print("The Values are :")

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

    roll_again=input("Roll the Dices Agian?")
