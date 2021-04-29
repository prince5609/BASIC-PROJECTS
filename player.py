import random
import math
class Player:
    def __init__(self,letter):
        self.letter=letter

    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        self.letter=letter
        super().__init__(letter)

    def get_move(self, game):
        moves = game.available_moves()
        square = random.choice(moves)
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        self.letter=letter
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square=input(self.letter + '\'s turn. input move(0,8) :')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Square try Again")

        return val


