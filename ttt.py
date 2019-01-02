from IPython.display import clear_output
import random

#position = int(input('Please enter a position'))

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Please choose "X" or "O":').upper()

    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)

player1_marker, player2_marker = player_input()

def place_marker(board, marker, position):
    if board[position]:
        print("Position is already taken. Please choose new position.")
        player_choice(board)
    else:
        board[position] = marker

def win_check(board, mark):
    win = False
    if board[1] == board[2] == board[3] == mark:
        win = True
    elif board[4] == board[5] == board[6] == mark:
        win = True
    elif board[7] == board[8] == board[9] == mark:
        win = True
    elif board[1] == board[4] == board[7] == mark:
        win = True
    elif board[2] == board[5] == board[8] == mark:
        win = True
    elif board[3] == board[6] == board[9] == mark:
        win = True
    elif board[1] == board[5] == board[9] == mark:
        win = True
    elif board[3] == board[5] == board[7] == mark:
        win = True

    return win

def choose_first():
    result = random.randint(1,2)
    if result == 1:
        first = 'player1'
    else:
        first = 'player2'
    return first
