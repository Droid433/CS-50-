"""
Tic Tac Toe Player
"""

import math
import sys
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
    numO = 0
    numX = 0
    for row in board:
        for choice in row:
            if choice == X:
                numX+=1
            elif choice == O:
                numO+=1
    #print(numX)
    #print(numO)
    if numX>numO:
        #print("X")
        return O
    elif numX == numO or board == initial_state():
        return X
    else:
        raise Exception("Turn not determined")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for r in range(0, len(board)):
        for c in range(0, len(board)):
            if board[r][c] == EMPTY:
                actions.add((r, c))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player1 = player(board)
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player1
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) == None:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    players = [X, O]
    winner = True
    for player in players:
        for r in range(0, len(board)):
            winner = True
            for c in range(0, len(board)):
                if board[r][c] != player:
                    winner = False
            if winner == True:
                if player == X:
                    return 1
                elif player == O:
                    return -1
        for c in range(0, len(board)):
            winner = True
            for r in range(0, len(board)):
                if board[r][c] != player:
                    winner = False
            if winner == True:
                if player == X:
                    return 1
                elif player == O:
                    return -1
        col = 0
        winner = True
        for r in range(0, len(board)): 
            if board[r][col] != player:   
                winner = False
            col+=1
        if winner == True:
            if player == X:
                return 1
            elif player == O:
                return -1
        winner = True
        col=0
        for r in range(0, len(board)):
            if board[2-r][col] != player:
                winner = False
            col+=1
        if winner == True:
            if player == X:
                return 1
            elif player == O:
                return -1
    if len(actions(board)) == 0:
        return 0
def max(move):
    #print("move")
    #print(move)
    if terminal(move):
        return utility(move)
    else:
        v=-10000
        for action2 in actions(move):
            if min(result(move, action2))>v:
                v = min(result(move, action2))
        return v
    
  #  for i in range(len(scores)):
   #     if scores[i] == None:
   #         scores[i] = 0
    
  #  max = -100000
   # for i in range(0, len(scores)):
    #    if(scores[i]>max):
     #       max = scores[i]
      #      score = i
    #return score
       
def min(move):
    #print("move")
    #print(move)
    if terminal(move):
        return utility(move)
    else:
        v=10000
        for action2 in actions(move):
            if max(result(move, action2))<v:
                v = max(result(move, action2))
        return v
    #for i in range(len(scores)):
     #  if scores[i] == None:
     #      scores[i] = 0
    # min = 1000000
    #for i in range(0, len(scores)):
    #    if(scores[i]<min):
     #       min = scores[i]
     #       score = i
    #return score
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if board == initial_state():
        return (2,2)
    scores = []
    actions1 = []
    
   # print("actions")
    #print(actions1)
    
    if terminal(board):
        return None
    if player(board) == X:
        turn = 1
        #print("X's turn")
    elif player(board) == O:
        #print("O's turn")
        turn = -1
    else:
        raise Exception("player not determined")
    for action in actions(board):
        #print("current board")
        #print(board)
        #print("examined action")
        #print(action)
        
        if turn == 1:

            
            actions1.append(action)
            scores.append(min(result(board, action)))
            
            
        elif turn == -1:
            
            actions1.append(action)
            scores.append(max(result(board, action)))
            
            

        #if terminal(result(board, action)):
         #   score = utility(result(board, action))
            #print("determined score")
            #print(score)
        #    scores.append(score)
        #else:
           # print("*")
            #print("expected board")
            #print(result(board, action))
         #   score = utility(result(result(board, action), minimax(result(board, action))))
          #  scores.append(score)

    #print("Possible actions ")
    #print(actions1)
    #print("relevant scores ")
    #print(scores)
    if turn == 1:
        #print(actions1[max(scores)])
        m = -1000
        v=0
        for score in range(len(scores)):
            if scores[score] > m:
                m = scores[score]
                v = score
        return actions1[v]
        
    elif turn == -1:
        m = 10000
        v=0
        for score in range(len(scores)):
            if scores[score] < m:
                m = scores[score]
                v = score
        return actions1[v]
    return None

        
    


       # for i in range(0, len(scores)):
        #    if isinstance(scores[i], int) and scores[i] == turn:
         #       optiMove = actions1[i]
        #return optiMove
    


