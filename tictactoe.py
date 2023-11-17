"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None





def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # initialize number of x and o variable in a state
    num_x = 0
    num_o = 0
    
    # if not terminal state. let's find out who's next to play
    for line in range(3):
        for i in range(3):
            if board[line][i] == X:
                num_x += 1
            elif board[line][i] == O:
                num_o += 1
    
    # print(f"i'm num_x {num_x}")
    return X if (num_x + num_o) % 2 == 0 else O
       



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # initialize the possible actions
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))

    return possible_actions
        

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # deep copy the board so as not to mutate the previous state (board)
    # an action-when a player makes a move returns X or O is taken on the board to produce a new state of the board
    
    # If the action is not valid raise an exception.
    if action not in actions(board):
        raise Exception("Not a valid input")

    deep_copied_board = copy.deepcopy(board)
    i,j = action
    deep_copied_board[i][j] = player(board)
        
    return deep_copied_board
   
        
        
 # if any of the players (x or o) meets the goal state condition, then there is a winner             
def check_rows_for_winner(board, player):
    for col in range(3):
        if board[col][0] == player and board[col][1] == player and board[col][2] == player:
            return True
    return False


def check_columns_for_winner(board, player):
    for line in range(3):
        if board[0][line] == player and board[1][line] == player and board[2][line] == player:
            return True
    return False
    
            
def check_left_to_right_diagonal(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    return False
    

def check_right_to_left_diagonal(board, player):
    if board[0][2] == player and board[1][1] ==player and board[2][0] == player:
        return True
    return False



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check the board current state with the goal state to see if there is a winner. there can only be one winner.
    if check_rows_for_winner(board, X) or check_columns_for_winner(board, X) or check_left_to_right_diagonal(board, X) or check_right_to_left_diagonal(board, X):
        return X
    elif check_rows_for_winner(board, O) or check_columns_for_winner(board, O) or check_left_to_right_diagonal(board, O) or check_right_to_left_diagonal(board, O):
        return O
    else:
        return 

  


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if the board is in its terminal state
    if winner(board)==X:
        return True
    if winner(board)==O:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    
def min_value(board):
    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v


def max_value(board):
    v = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """ 

    if terminal(board):
        return None
    
    # max player (X)
    elif player(board) == X:
        new_array = []
        for action in actions(board):
            new_array.append([min_value(result(board,action)), action])
        return sorted(new_array, key=lambda x: x[0], reverse=True)[0][1]
   
    
    # min player (X)
    elif player(board) == O:
        new_array = []
        for action in actions(board):
            new_array.append([max_value(result(board,action)), action])
        return sorted(new_array, key=lambda x: x[0])[0][1]
    
