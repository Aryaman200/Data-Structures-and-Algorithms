def sudoku_solver(board):
    def is_valid(r, c, d):
        for i in range(9):
            if board[r][i] == d or board[i][c] == d:
                return False
            if board[3*(r//3)+i//3][3*(c//3)+i%3] == d:
                return False
        return True
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for d in '123456789':
                        if is_valid(i,j,d):
                            board[i][j] = d
                            if solve(): return True
                            board[i][j] = '.'
                    return False
        return True
    solve()
    return board