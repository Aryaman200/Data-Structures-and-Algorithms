def longest_substring_without_repeating(s):
    used = {}
    res, l = 0, 0
    for i, c in enumerate(s):
        if c in used and l <= used[c]:
            l = used[c] + 1
        used[c] = i
        res = max(res, i - l + 1)
    return res

def max_sum_subarray_of_size_k(arr, k):
    curr_sum = sum(arr[:k])
    max_sum = curr_sum
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

def minimum_window_substring(s, t):
    from collections import Counter
    need = Counter(t)
    have, required = {}, len(need)
    l = r = 0
    formed = 0
    res = (float('inf'), 0, 0)
    while r < len(s):
        c = s[r]
        have[c] = have.get(c,0) + 1
        if c in need and have[c] == need[c]:
            formed += 1
        while l <= r and formed == required:
            if r-l+1 < res[0]:
                res = (r-l+1, l, r)
            have[s[l]] -= 1
            if s[l] in need and have[s[l]] < need[s[l]]:
                formed -= 1
            l += 1
        r += 1
    return "" if res[0] == float('inf') else s[res[1]:res[2]+1]

def container_with_most_water(height):
    l, r = 0, len(height)-1
    res = 0
    while l < r:
        res = max(res, min(height[l], height[r]) * (r-l))
        if height[l] < height[r]: l += 1
        else: r -= 1
    return res
