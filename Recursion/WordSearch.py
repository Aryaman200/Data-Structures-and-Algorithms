def word_search(board, word):
    m, n = len(board), len(board[0])
    def dfs(i, j, k):
        if k == len(word): return True
        if not (0 <= i < m and 0 <= j < n and board[i][j] == word[k]):
            return False
        tmp, board[i][j] = board[i][j], '#'
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            if dfs(i+di, j+dj, k+1): return True
        board[i][j] = tmp
        return False
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0): return True
    return False