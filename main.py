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
                return score
    #check if player win in other diagonal
    for i in range(3, 6):
        for j in range(4):
            line1 = [board[i-k][j+k] for k in range(4)] 
            if line1 == [player,player,player,player]:
                score +=100
                return score  
    # check if the player win horizontal by connecting 4 in one row
    for i in range(6):  # we have 6 rows
        for j in range(4):
            # list that store 4 element that get out from condation
            line2 = [board[i][j + k] for k in range(4)]
            if line2 == [player, player, player, player]:
                score += 100
                return score

    # check if the player win vertical by connect 4 in one column
    for j in range(7):  # we have 6 rows
        for i in range(3):
            # list that store 4 element that get out from condation
            line3 = [board[i + k][j] for k in range(4)]
            if line3 == [player, player, player, player]:
                score += 100
                return score

    return score


#function get all possible moves that you can do
def Move_Options(board):
    avalibale_move =[]
    for j in range (7):
        if board[0][j] == 0:
            for i in reversed(range(6)):
                if board[i][j] == 0:
                    avalibale_move.append((i,j))
                    break
    return avalibale_move   

#implement minmax algorithm with alpha&beta purning 
def MinMax_Algorithm(board , depth , maxstate,alpha,beta):
    moves = Move_Options(board)
    if (depth ==0):
        return Get_score(board,AI_Agent)  
    if (len(moves) == 0):
        return Get_score(board,AI_Agent)
    if(Get_score(board,AI_Agent) == 100 ):
        return Get_score(board,AI_Agent)

    #if maxstate is true that means we are in max mode
    if (maxstate):
        for current_move in moves:
            new_board = copy.deepcopy(board)
            #moves is represent as pair of 2 numbers(i,j), i for rows and j for columns
            # move[0] represent first number in pair (row number)
            # move[1] represent second number in pair (culumn number)
            new_board[current_move[0]][current_move[1]] = AI_Agent 
            #call the algorithm recursivally with depth-1 and in other mode(that mean if we in max level we call min level and so on..)
            value = MinMax_Algorithm(new_board,depth-1,False,alpha,beta)
            alpha = max(value,alpha)
            if alpha >= beta:
                break
        return alpha 
    #if maxstate is false we are in min mode
    else:
        for current_move in moves:
             new_board =copy.deepcopy(board)
             new_board[current_move[0]][current_move[1]] = Computer
             value = MinMax_Algorithm(new_board,depth-1,True,alpha,beta)
             beta = min(beta,value)
             if alpha >= beta:
                break
        return beta