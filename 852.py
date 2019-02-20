def peakIndexInMountainArray(A: 'List[int]'):
    max = A[0]
    index = 0
    for i in range(0, len(A)):
        if A[i] > max:
            max = A[i]
            index = i

    return index

print(peakIndexInMountainArray([0,2,1,0]))


