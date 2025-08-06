def n_queens(n):
    res = []
    board = [["."]*n for _ in range(n)]
    def is_valid(r, c):
        for i in range(r):
            if board[i][c] == 'Q': return False
            if c - (r - i) >= 0 and board[i][c - (r - i)] == 'Q': return False
            if c + (r - i) < n and board[i][c + (r - i)] == 'Q': return False
        return True
    def solve(row):
        if row == n:
            res.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'
    solve(0)
    return res
