import random


def roll_dice():
    print("Welcome")
    operation = input("Do you want to roll the dice, Y for yes and N for no? :")
    while True:
        if operation != "N":
            if operation == "Y":
                print(random.randint(1, 6))
                print(random.randint(1, 6))
                ask = input("Do you want to roll it again Y for yes &  N for Y? :")
                if ask == "Y":
                    continue
                elif ask == "N":
                    print("ok! Good Bye")
                    break
        else:
            print("ok! Good Bye")
            break


roll_dice()
