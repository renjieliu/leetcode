def duplicateZeros(arr: 'List[int]'):
    """
    Do not return anything, modify arr in-place instead.
    """
    l = len(arr)
    i = 0
    while i < l:
        if arr[i] ==0:
            arr.insert(i+1, 0)
            arr.pop()
            i+=2
        else:
            i+=1

    return arr

print(duplicateZeros([1,0,2,3,0,4,5,0]))
print(duplicateZeros([1,2,3]))