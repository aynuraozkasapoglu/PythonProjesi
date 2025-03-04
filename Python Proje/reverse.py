def reversed_list (arr):
    
    for i in range(len(arr)):
        if type(arr[i]) == type([]):
            arr[i] = arr[i][::-1]
            reversed_list(arr[i])
    
    return (arr[::-1])

"""
Sample Outputs:
arr = [1,2,[3,4,5],[6,7[8,9,10]],11,12]
arr = [1,[1, 2], [3, 4], 20, 45, [5, 6, 7], 10]

"""
arr = [1,2,[3,4,5],[6,7,[8,9,10]],11,12]
print(reversed_list(arr))