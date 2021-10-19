def sortArrayByParity(A: 'List[int]'):
    output1 = []
    output2 = []
    for i in A:
        if int(i) % 2 == 0:
            output1.append(i)
        else:
            output2.append(i)
    return output1 + output2

print(sortArrayByParity([3,1,2,4]))