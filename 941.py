def validMountainArray(A: 'List[int]'):
    if len(A) < 3:
        return False

    max = A[0]
    pos = 0
    for i in range(len(A)):
        if A[i]> max:
            max = A[i]
            pos = i

    if pos ==0 or pos == len(A)-1:
        return False


    for i in range(len(A)-1):
        if i < pos and A[i]>=A[i+1]:
            return False
        if i>=pos and A[i+1]>=A[i]:
            return False

    return True

print(validMountainArray([2,1]))
print(validMountainArray([3,5,5]))
print(validMountainArray( [0,3,2,1]))

