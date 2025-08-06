import heapq

def heapify(arr):
    heapq.heapify(arr)
    return arr

def kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]

def kth_smallest(arr, k):
    return heapq.nsmallest(k, arr)[-1]

def merge_k_sorted_arrays(arrays):
    from heapq import heappush, heappop
    h = []
    res = []
    for i, arr in enumerate(arrays):
        if arr:
            heappush(h, (arr[0], i, 0))
    while h:
        val, i, j = heappop(h)
        res.append(val)
        if j+1 < len(arrays[i]):
            heappush(h, (arrays[i][j+1], i, j+1))
    return res

def median_of_stream(nums):
    from heapq import heappush, heappop
    small, large = [], []
    res = []
    for n in nums:
        heappush(small, -heappush(large, n) if large and n > large[0] else -n)
        if len(small) > len(large):
            heappush(large, -heappop(small))
        if len(small) == len(large):
            res.append((large[0] - small[0]) / 2)
        else:
            res.append(large[0])
    return res
