from player import HumanPlayer , RandomComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board=[" " for _ in range(9)]     # we are using a single list to represent a board
        self.current_winner = None

    def print_board(self):
         # here we are getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("|" + "|".join(row) + "|")


    @staticmethod
    def print_board_nums():
        # 0|1|2.....etc for each row
        for j in range(3):
            number_board = []
            for i in range(j*3,(j+1)*3):
                number_board.append(str(i))
            print("|" + "|".join(number_board) + "|")

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):          # if [x,x,o]  -> (0,x) (1,x)  (2,o)
            if spot == " ":
                moves.append(i)
        return moves

    def empty_square(self):
        # it will return an bollean of weather empty " " is there or not
        return " " in self.board

    def num_empty_square(self):
        return self.board.count(" ")

    def make_move(self,square,letter):

        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        # let's check row first
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # let's check column now
        col_ind = square%3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # let's check now diagonal also
        # only even number are there in diagonal.......0,2,4,6,8
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all these fails then no winner
        return False


def play(game,x_player,o_player,print_game = True):
    if print_game:
        game.print_board_nums()

    letter="x"

    while game.empty_square():
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)



        if game.make_move(square,letter):
            if print_game:
                print(letter +f" make a move to square {square}")
                game.print_board()
                print(" ")

            if game.current_winner:
                if print_game:
                    print(letter + " wins !")
                return letter
            letter = "o" if letter == "x" else "x"

        elif print_game:
            print("it's a tie")

if __name__ == '__main__':
    x_player=HumanPlayer("x")
    o_player=RandomComputerPlayer("o")
    t=TicTacToe()
    play(t,x_player,o_player, print_game=True)









