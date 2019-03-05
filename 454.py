def fourSumCount(A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]'):
    result = {}
    cnt = 0

    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] + B[j] not in result.keys():
                result[A[i] + B[j]] = 0
            result[A[i] + B[j]] +=1

    for x in range(len(C)):
        for y in range(len(D)):
            if -1*(C[x] + D[y]) in result.keys():
                cnt += result[-1*(C[x] + D[y])]



    # result = []
    # for i in range(len(A)):
    #     for j in range(len(C)):
    #         result.append(A[i] + C[j])
    #
    # for i in range(len(B)):
    #     for j in range(len(D)):
    #         if -(B[i] + D[j]) in result:
    #             cnt+=1
    #
    # result = []
    # for i in range(len(A)):
    #     for j in range(len(D)):
    #         result.append(A[i] + D[j])
    #
    # for i in range(len(B)):
    #     for j in range(len(C)):
    #         if -(B[i] + C[j]) in result:
    #             cnt+=1


    return cnt

# print(fourSumCount([ 1, 2]
# ,[-2,-1]
# ,[-1, 2]
# ,[ 0, 2]))

print(fourSumCount([-1,-1]
,[-1,1]
,[-1,1]
,[1,-1]))