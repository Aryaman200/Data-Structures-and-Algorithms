def generate_subsets_bits(nums):
    n = len(nums)
    res = []
    for i in range(1<<n):
        subset = [nums[j] for j in range(n) if (i>>j)&1]
        res.append(subset)
    return res