
def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0]*(n2+1) for _ in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i]==s2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[n1][n2]