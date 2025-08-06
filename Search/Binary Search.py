def user_input():
    global arr 
    arr = []
    global target

    n = int(input("Enter the Number of Elements: "))
    i = 0 
    while i < n:
        element = int(input(f"Enter the {i}th Element: "))
        arr.append(element)
        i += 1

    arr.sort()  
    target = int(input("Enter the Number you want to search for: "))
    return arr, target

def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first

def find_last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last

def binary_search_multiple_occurrences(arr, target):
    first = find_first_occurrence(arr, target)
    last = find_last_occurrence(arr, target)

    if first == -1:
        return []  
    return list(range(first, last + 1))  


arr, target = user_input()
indices = binary_search_multiple_occurrences(arr, target)

if indices:
    print("Target found at indices:", indices)
    print("Values:", [arr[i] for i in indices])
else:
    print("Target not found.")
