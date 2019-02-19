def sortedSquares(A: 'List[int]'):
    output = []
    for i in A:
        output.append(int(i)**2)

    output.sort()
    return output

print(sortedSquares([-4,-1,0,3,10]))