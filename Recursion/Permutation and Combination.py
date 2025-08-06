def generate_permutations(nums):
    res = []
    def backtrack(used, path):
        if len(path) == len(nums):
            res.append(list(path))
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                backtrack(used, path + [nums[i]])
                used[i] = False
    backtrack([False]*len(nums), [])
    return res

def generate_combinations(nums, k):
    res = []
    def backtrack(start, path):
        if len(path) == k:
            res.append(list(path))
            return
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    backtrack(0, [])