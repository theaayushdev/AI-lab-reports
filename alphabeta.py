#ques no .5 lab report alpha beta

import math


def evaluate(board):
    win_states = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for (x, y, z) in win_states:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return 10 if board[x] == "X" else -10
    return 0

def possible_moves(board):
    return [i for i in range(9) if board[i] == " "]

def make_move(board, move, player):
    board[move] = player

def undo_move(board, move):
    board[move] = " "

def alpha_beta(board, depth, alpha, beta, is_maximizer):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not possible_moves(board):
        return 0

    if is_maximizer:
        best = -math.inf
        for move in possible_moves(board):
            make_move(board, move, "X")
            best = max(best, alpha_beta(board, depth + 1, alpha, beta, False))
            undo_move(board, move)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for move in possible_moves(board):
            make_move(board, move, "O")
            best = min(best, alpha_beta(board, depth + 1, alpha, beta, True))
            undo_move(board, move)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = None
    for move in possible_moves(board):
        make_move(board, move, "X")
        move_val = alpha_beta(board, 0, -math.inf, math.inf, False)
        undo_move(board, move)
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move

board = [" "] * 9
best_move = find_best_move(board)
print("The best move for Maximizer is:", best_move)
