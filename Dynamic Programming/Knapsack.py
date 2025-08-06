def knapsack_01(wt, val, W):
    n = len(wt)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(W+1):
            if wt[i-1]<=w:
                dp[i][w]=max(dp[i-1][w],val[i-1]+dp[i-1][w-wt[i-1]])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]
