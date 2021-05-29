import random


def guess_computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or can be high also as low=high
        feedback = str(input(f"hey is {guess} too low(l) or too high(h) or correct(c)?? :"))
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1

    if feedback == 'c':
        print("hey computer guessed the number correctly")


guess_computer(int(input("Enter the value of higher number :")))
