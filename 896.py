def isMonotonic(A: 'List[int]'):

    if len(A) == 1:
        return True

    cnt = 1

    for i in range(1, len(A)):
        if A[i] - A[i-1] >= 0:
            cnt += 1

    if cnt == len(A):
        return True

    cnt = 1

    for i in range(1, len(A)):
        if A[i] - A[i - 1] <= 0:
            cnt += 1

    if cnt == len(A):
        return True

    return False


print(isMonotonic([1,3,2]))

