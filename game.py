class TicTacToe:
    def __init__(self):
        self.board=[" " for _ in range(9)]    # we will use a list to rep a 3*3 board
        self.current_winner=None    # keep track


    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("|"+"|".join(row)+"|")

    @staticmethod
    def print_board_num():
        # 0|1|2....[tells us what number corresponds to what box]
        for j in range(3):
            for i in range(j*3,(j+1)*3):
                number_board=str(i)
                for row in number_board:
                    print("|" + "|".join(row) + "|")

    def available_moves(self):
        moves=[]
        for (i,spot) in enumerate(self.board):
            if spot== " ":
                moves.append(i)
        return moves
    def empty_square(self):
        return " " in self.board
    def num_empty_square(self):
        return len(self.available_moves())
def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_board_num()

    letter="x"
    while game.empty_square():
        # get the move from appropriate player

        if letter=="o":
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)

