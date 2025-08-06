def partition_equal_subset_sum(nums):
    s = sum(nums)
    if s%2: return False
    target = s//2
    dp = set([0])
    for n in nums:
        next_dp = dp.copy()
        for t in dp:
            if t+n==target: return True
            next_dp.add(t+n)
        dp = next_dp
    return target in dp
