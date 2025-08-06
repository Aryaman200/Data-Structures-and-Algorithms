def lis(nums):
    dp = []
    import bisect
    for n in nums:
        idx = bisect.bisect_left(dp, n)
        if idx == len(dp): dp.append(n)
        else: dp[idx] = n
    return len(dp)
