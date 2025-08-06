def matrix_chain_multiplication(arr):
    n = len(arr) - 1
    dp = [[0]*n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j],
                    dp[i][k]+dp[k+1][j]+arr[i]*arr[k+1]*arr[j+1])
    return dp[0][n-1]