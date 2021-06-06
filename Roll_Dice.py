import random


def roll_dice():
    print("Welcome")
    operation = input("Do you want to roll the dice, Y for yes and N for no? :")
    while operation != "N" and operation != "n":
        if operation == "Y" or operation == "y" :
            print(random.randint(1, 6))
            print(random.randint(1, 6))
            ask = input("Do you want to roll it again Y for yes &  N for Y? :")
            if ask == "Y" or ask == "y":
                continue
            elif ask == "N" or ask == "n":
                break
        else:
            print("Invalid Input try again")
            operation = input("Do you want to roll the dice, Y for yes and N for no? :")

    return print("Ok! Good Bye")


roll_dice()
