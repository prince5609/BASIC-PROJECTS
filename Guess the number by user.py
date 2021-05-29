import random


def guess_user(x):
    guess = 0
    guess_count = 0
    guess_limit = 5
    out_of_guess = False
    random_number = random.randint(1, x)
    while guess != random_number and not out_of_guess:
        if guess_limit > guess_count:
            guess = int(input(f"Enter your guess between 1 and {x} :"))
            guess_count = guess_count + 1
            if guess < random_number:
                print("Sorry you guessed a low number, try another")
            elif guess > random_number:
                print("Sorry you guessed a higher number,try again")
        else:
            out_of_guess = True
    if out_of_guess:
        print("Hey you reached the limit of guess & you loose")
    else:
        print("Hey you guessed the number correctly & you win")


guess_user(int(input("Enter the end value of your range :")))
