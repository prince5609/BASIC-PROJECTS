# rock>scissor  scissor>paper  paper>rock
import random


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') and (
            player == 'p' and opponent == 'r'):
        return True


def play():
    user = str(input("enter your choice rock(r) or scissor(s) or paper(p) :"))
    computer = random.choice(['r', 's', 'p'])
    if user == computer:
        return "tie"
    if is_win(user, computer):
        return "you won"
    return "you lost"


print(play())
