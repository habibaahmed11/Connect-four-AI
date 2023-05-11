import random
import copy

# define min and max for alpha and beta
MAX = float('-inf')  # for alpha = -infinity
MIN = float('inf')  # for beta  = infinity
# define the two players
AI_Agent = "R"
Computer = "Y"


# print board like connect 4 game
def print_board(board):
    for row in range(6):
        print("| ", end="")
        for col in range(7):
            print(board[row][col], "| ", end="")
        print()
    print("-----------------------------")


# define board of 2 dimensions with 6 rows and 7 colums to create connect 4 game
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


# define function that calc score of one of players
def Get_score(board, player):
    score = 0
    # check if player wins in the digonal
    for i in range(3):
        for j in range(4):
            # its list of 4 element which i loop in board to get if there 4 element in one digonal
            # we loop with k time becouse if there 4 connected that mean you win
            line1 = [board[i + k][j + k] for k in range(4)]
            if line1 == [player, player, player, player]:
                score += 100

    # check if the player win horizontal by connect 4 in one row
    for i in range(6):  # we have 6 rows
        for j in range(4):
            # list that store 4 element that get out from condation
            line2 = [board[i][j + k] for k in range(4)]
            if line2 == [player, player, player, player]:
                score += 100

                # check if the player win vertical by connect 4 in one column
    for j in range(7):  # we have 6 rows
        for i in range(3):
            # list that store 4 element that get out from condation
            line3 = [board[i + k][j] for k in range(4)]
            if line3 == [player, player, player, player]:
                score += 100

    return score


