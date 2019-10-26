def sortedSquares(A: 'List[int]'):
    output = []
    i, j = 0, len(A) - 1
    while i <= j:
        if abs(A[i]) < abs(A[j]):
            output.append(A[j] ** 2)
            j -= 1
        else:
            output.append(A[i] ** 2)
            i += 1

    return output[::-1]

    # previous codes

    # output = []
    # for i in A:
    #     output.append(int(i)**2)
    #
    # output.sort()
    # return output


print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))