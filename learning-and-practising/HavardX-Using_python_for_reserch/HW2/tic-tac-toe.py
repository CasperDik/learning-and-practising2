import numpy as np
import random

random.seed(1)

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

def place(board, player, position):
    if board[position] == 0:
        board[position] = player

def possibilities(board):
    possible = np.where(board == 0)
    return list(zip(possible[0], possible[1]))

def random_place(board, player):
    if len(possibilities(board)) > 0:
        selection = random.choice(possibilities(board))
        place(board, player, selection)
        #print(selection)
    return board

def row_win(board, player):
    for i in range(3):
        if np.array_equal(board[i], [player, player, player]):
            return True
    return False

def col_win(board, player):
    for i in range(3):
        if np.array_equal(board[:,i], [player, player, player]):
            return True
    return False

def diag_win(board, player):
    if np.array_equal(board.diagonal(), [player, player, player]):
        return True
    elif np.array_equal(np.fliplr(board).diagonal(), [player, player, player]):
        return True
    return False

def evaluate(board):
    winner = 0
    for player in [1,2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player) == True:
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board = create_board()
    for i in range(5):
        for j in [1,2]:
            if evaluate(board) != 0:
                return evaluate(board)
            else:
                random_place(board, j)


def play_strategic_game():
    board = create_board()
    board[1,1] = 1
    for i in range(4):
        for j in [1,2]:
            if evaluate(board) != 0:
                return evaluate(board)
            else:
                random_place(board, j)


results = []
for i in range(10):
    x = play_strategic_game()
    results.append(x)

print(results.count(None))
print(results.count(1))
