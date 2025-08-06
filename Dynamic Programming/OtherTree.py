def dp_trees(root):
    if not root: return 0
    left = max(0, dp_trees(root.left))
    right = max(0, dp_trees(root.right))
    return root.val + max(left, right)

def dp_grids(grid):
    n, m = len(grid), len(grid[0])
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(m):
            if i>0:
                dp[i][j] = max(dp[i][j], dp[i-1][j]+grid[i][j])
            if j>0:
                dp[i][j] = max(dp[i][j], dp[i][j-1]+grid[i][j])
    return dp[n-1][m-1]