def transpose(A: 'List[List[int]]'):
    c_cnt = len(A[0])
    r_cnt = len(A)
    output = []

    for i in range(0, c_cnt):
        output.append([])
        for j in range(0, r_cnt):
            output[i].append(A[j][i])

    return output

print(transpose([[1,2,3],[4,5,6]]))



