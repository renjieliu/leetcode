def missingNumber(arr: 'List[int]'):
    pg = (arr[-1] - arr[0]) // len(arr)  # find the supposed progression of the array
    if pg  ==0 :
        return arr[0]
    for i in range(1, len(arr)):  # find the missing one
        if arr[i] - arr[i - 1] != pg:
            return arr[i - 1] + pg



print(missingNumber([5,7,11,13]))
print(missingNumber([15,13,12]))
print(missingNumber([5,5,5]))