def longestArithSeqLength(A: 'List[int]'):
    if len(A) ==2:
        return 2
    else:
        output = 2
        arr = [None] * len(A)
        arr[0] = {'DUMMY':2}
        #arr[1] = {A[1]-A[0]:2}
        for i in range(1, len(A)):
            arr[i] = {}
            for j in range(i-1, -1,-1):
                diff = A[i] - A[j]
                if diff not in arr[j] and diff not in arr[i]:
                    arr[i][diff] = 2
                elif diff not in arr[i] and diff in arr[j] :
                    arr[i][diff]= arr[j][diff]+1

                #print(arr)

                output = max(output,arr[i][diff])

    return output


print(longestArithSeqLength([3,6,9,12]))
print(longestArithSeqLength([9,4,7,2,10]))
print(longestArithSeqLength([20,1,15,3,10,5,8]))
print(longestArithSeqLength([22,8,57,41,36,46,42,28,42,14,9,43,27,51,0,0,38,50,31,60,29,31,20,23,37,53,27,1,47,42,28,31,10,35,39,12,15,6,35,31,45,21,30,19,5,5,4,18,38,51,10,7,20,38,28,53,15,55,60,56,43,48,34,53,54,55,14,9,56,52]))
# #6

