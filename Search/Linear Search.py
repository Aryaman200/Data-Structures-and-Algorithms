def user_input():
    global arr 
    arr = []
    global target
    
    n = int ( input( "Enter the Number of Elements: "))
    i = 0 
    while i < n:
        element = int(input(f"Enter the {i}th Element: "))
        arr.append(element)
        i+=1
    target = int( input("Enter the Number you want to search for: "))
    return arr, target

def linear_search(arr, target):
    index = -1
    count = 0
    idx_lst = []
    flag = 0 
    for element in arr:
        index +=1
        if element == target: 
             idx_lst.append(index)
             count +=1
             flag = 1
    return idx_lst, count , flag

inputt = list(user_input())
result = linear_search(inputt[0], inputt[1])
list(result)

if result[2] != 0:
    print(f'{target} found at index(s): {result[0]}, with count: {result[1]}')
else:
    print("Element not found.")