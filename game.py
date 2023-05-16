from board import Board
import time
import random
from gamealgorithms import make_move, is_terminal_game, winning_move, Move_Options


# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()
    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        #board.print_grid(game_board)

        # YOUR CODE GOES HERE
        column = make_move(game_board, 4, 1, "alpha")

        print("made move")
        while(column==6):
            moves=Move_Options(game_board)
            column=random.choice(moves)[1]

        #board.select_column(column)
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        #column = random.randint(0, 6)
        #print(column)
        board.select_column(column)

        time.sleep(3)

if __name__ == "__main__":
    main()
