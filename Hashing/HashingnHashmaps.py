def frequency_count(arr):
    from collections import Counter
    return Counter(arr)

def contains_duplicate(arr):
    return len(arr) != len(set(arr))

def longest_consecutive_subsequence(arr):
    s = set(arr)
    longest = 0
    for elem in s:
        if elem-1 not in s:
            cur = elem
            streak = 1
            while cur+1 in s:
                cur += 1
                streak += 1
            longest = max(longest, streak)
    return longest

def two_sum(arr, k):
    lookup = {}
    for i, num in enumerate(arr):
        if k - num in lookup:
            return [lookup[k-num], i]
        lookup[num] = i
    return []

def subarray_sum_equals_k(nums, k):
    from collections import defaultdict
    count, res, pre = defaultdict(int), 0, 0
    count[0] = 1
    for n in nums:
        pre += n
        res += count[pre - k]
        count[pre] += 1
    return res

def group_anagrams(words):
    from collections import defaultdict
    d = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        d[key].append(word)
    return list(d.values())

def find_all_duplicates(arr):
    res = []
    for num in arr:
        idx = abs(num) - 1
        if arr[idx] < 0:
            res.append(abs(num))
        else:
            arr[idx] *= -1
    return res
