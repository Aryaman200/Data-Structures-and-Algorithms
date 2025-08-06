def coin_change_min(coins, amt):
    dp = [float('inf')] * (amt+1)
    dp[0] = 0
    for c in coins:
        for x in range(c, amt+1):
            dp[x] = min(dp[x], dp[x-c] + 1)
    return dp[amt] if dp[amt]!=float('inf') else -1

def coin_change_ways(coins, amt):
    dp = [0]*(amt+1)
    dp[0]=1
    for c in coins:
        for x in range(c, amt+1):
            dp[x] += dp[x-c]
    return dp[amt]
