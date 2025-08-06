def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

def two_non_repeating(nums):
    xor = 0
    for n in nums:
        xor ^= n
    set_bit = xor & -xor
    x = y = 0
    for n in nums:
        if n & set_bit:
            x ^= n
        else:
            y ^= n
    return (x, y)