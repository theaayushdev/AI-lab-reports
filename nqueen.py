# lab 1 N-Queens Problem Without Recursion

def is_safe(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve_n_queens_iterative(N):
    stack = []
    row = 0
    board = [-1] * N

    while row < N:
        placed = False
        for col in range(board[row] + 1, N):
            if is_safe(board, row, col):
                board[row] = col
                stack.append((row, col))
                placed = True
                break

        if not placed:
            if not stack:
                print("No solution found.")
                return
            row, col = stack.pop()
            board[row] = -1
            row -= 1
        else:
            row += 1

    print("Solution:", board)


solve_n_queens_iterative(4)
