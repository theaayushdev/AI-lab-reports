#minmax question
import math

def evaluate(board):
    win_states = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    
    for (x, y, z) in win_states:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return 10 if board[x] == "X" else -10
    return 0 if " " in board else None

def min_max(board, is_maximizer):
    score = evaluate(board)
    if score is not None:
        return score

    if is_maximizer:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, min_max(board, False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, min_max(board, True))
                board[i] = " "
        return best


board = [" "] * 10
print("Best score:", min_max(board, True))
