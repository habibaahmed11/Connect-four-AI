import tkinter as tk
import random
import copy
from tkinter import *
from tkinter import ttk

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
    
    
#define the simple version of min max algorithm
def Simple_MinMax_Algorithm(board ,depth , maxstate):
    moves = Move_Options(board)
    if (depth ==0):
        return Get_score(board,AI_Agent)  
    if (len(moves) == 0):
        return Get_score(board,AI_Agent)
    #if maxstate is true that means we are in max mode
    if (maxstate):
        max_val = MAX
        for current_move in moves:
            new_board = copy.deepcopy(board)
            #moves is represent as pair of 2 numbers(i,j), i for rows and j for columns
            # move[0] represent first number in pair (row number)
            # move[1] represent second number in pair (culumn number)
            new_board[current_move[0]][current_move[1]] = AI_Agent 
            #call the algorithm recursivally with depth-1 and in other mode(that mean if we in max level we call min level and so on..)
            value = Simple_MinMax_Algorithm(new_board,depth-1,False)
            max_val = max(max_val,value)
        return max_val     
    #if maxstate is false we are in min mode
    else:
        min_val = MIN
        for current_move in moves:
             new_board =copy.deepcopy(board)
             new_board[current_move[0]][current_move[1]] = Computer
             value = Simple_MinMax_Algorithm(new_board,depth-1,True)
             min_val = min(min_val,value)
        return min_val
    
def make_move(board,depth,player,type):
    moves = Move_Options(board)
    if(len(moves)== 0):
        return
    best_move = None
    best_score = MAX
    for current_move in moves:
        new_board = copy.deepcopy(board)
        new_board[current_move[0]][current_move[1]] = player
        if type == "simple":
            value = Simple_MinMax_Algorithm(new_board,depth,True)
        else:
            value = MinMax_Algorithm(new_board,depth,True,MAX,MIN)

        if value > best_score :
            best_score = value
            best_move = current_move
    print("AI Agent Select Best Move = ",best_move)        
    board[best_move[0]][best_move[1]] = player
    
    
    
    #GUI
    root = tk.Tk() #create root window
root.title("connect four game")  #name of root window
root.geometry("300x150")   #size of root window

        # Create algorithm type label and it's option
label = tk.Label(root, text="Algorithm Type:")
label.pack()
algorithm_type_var = tk.StringVar()  #variable to store selected optin
options_menu = tk.OptionMenu(root, algorithm_type_var, "Minimax algorithm", "Alpha-Beta Pruning algorithm")
options_menu.pack()

        # Create difficulty level label and it's option
label = tk.Label(root, text="Difficulty Level:")
label.pack()
difficulty_level_var = tk.StringVar() #variable to store selected optin
options_menu = tk.OptionMenu(root, difficulty_level_var, "Easy", "Medium", "Hard")
options_menu.pack()

#function to get selected algorithm type and difficulty level and print them with start the connect four game
def start_game():
    algorithm_type = algorithm_type_var.get()
    difficulty_level = difficulty_level_var.get()

    if algorithm_type == "Minimax algorithm":
        type = "simple"
    else:
        type = "alpha-beta"

    # Start the game with the selected algorithm type and difficulty level
    print("Starting game with algorithm type:", algorithm_type, "and difficulty level:", difficulty_level)
    Game(board, 3, type)


        # Create submit button when clicked then call start game function to start the game
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

         # Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)  #add the menu bar to the root window

            # Create exit menu
exit_menu = tk.Menu(menu_bar, tearoff=0)  #tearoff arg to prevent move
menu_bar.add_cascade(label="Exit", menu=exit_menu)  #add exit menu to menu bar

        # Create help menu
help_menu = tk.Menu(menu_bar, tearoff=0)  #tearoff arg to prevent move 
help_menu.add_command(label="About")  #add about menu to help menu
menu_bar.add_cascade(label="Help", menu=help_menu)  #add help menu to menu bar

#wait to user input and update 
root.mainloop()
       
