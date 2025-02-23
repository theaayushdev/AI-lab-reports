# ques no. 2 N-Queens Problem Using Backtracking

def is_safe(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve_n_queens_backtracking(N, board=[], row=0):
    if row == N:
        print("output:", board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            if solve_n_queens_backtracking(N, board, row + 1):
                return True
            board.pop()

    return False


solve_n_queens_backtracking(4)
