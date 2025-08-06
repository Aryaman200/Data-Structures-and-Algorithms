def reverse_array(arr):
    arr.reverse()
    return arr

def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    arr[:] = arr[d:] + arr[:d]
    return arr

def kadane(arr):
    max_sum = curr = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)
        max_sum = max(max_sum, curr)
    return max_sum

def sliding_window_max_sum(arr, k):
    n = len(arr)
    max_sum = curr = sum(arr[:k])
    for i in range(k, n):
        curr = curr + arr[i] - arr[i-k]
        max_sum = max(max_sum, curr)
    return max_sum

def anagram_finder(s, p):
    from collections import Counter
    res = []
    np, ns = len(p), len(s)
    p_count = Counter(p)
    s_count = Counter(s[:np-1])
    for i in range(np-1, ns):
        s_count[s[i]] +=1
        if s_count == p_count:
            res.append(i-np+1)
        s_count[s[i-np+1]] -=1
        if s_count[s[i-np+1]] == 0: del s_count[s[i-np+1]]
    return res

def prefix_sum(arr):
    res, total = [], 0
    for x in arr:
        total += x
        res.append(total)
    return res

def merge_intervals(intervals):
    intervals.sort()
    res = []
    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1], i[1])
    return res

def two_sum(arr, target):
    seen = set()
    for x in arr:
        if target - x in seen:
            return True
        seen.add(x)
    return False

def three_sum(arr):
    res = []
    arr.sort()
    n = len(arr)
    for i in range(n):
        if i == 0 or arr[i] != arr[i-1]:
            l, r = i+1, n-1
            while l < r:
                tot = arr[i] + arr[l] + arr[r]
                if tot == 0:
                    res.append([arr[i], arr[l], arr[r]])
                    l += 1
                    while l < r and arr[l] == arr[l-1]: l += 1
                elif tot < 0:
                    l += 1
                else:
                    r -= 1
    return res

def container_with_most_water(height):
    l, r = 0, len(height)-1
    mx = 0
    while l < r:
        mx = max(mx, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]: l += 1
        else: r -= 1
    return mx

def dutch_national_flag(arr):
    l, m, r = 0, 0, len(arr)-1
    while m <= r:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1; m += 1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[r] = arr[r], arr[m]
            r -= 1
    return arr

def trapping_rain_water(height):
    n = len(height)
    if n == 0: return 0
    lmax, rmax = [0]*n, [0]*n
    lmax[0], rmax[-1] = height[0], height[-1]
    for i in range(1, n): lmax[i] = max(lmax[i-1], height[i])
    for i in range(n-2, -1, -1): rmax[i] = max(rmax[i+1], height[i])
    water = 0
    for i in range(n):
        water += min(lmax[i], rmax[i]) - height[i]
    return water

def longest_substring_k_distinct(s, k):
    from collections import defaultdict
    n, l, res = len(s), 0, 0
    count = defaultdict(int)
    for r in range(n):
        count[s[r]] += 1
        while len(count) > k:
            count[s[l]] -= 1
            if count[s[l]] == 0:
                del count[s[l]]
            l += 1
        res = max(res, r - l + 1)
    return res