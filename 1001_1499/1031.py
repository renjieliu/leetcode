def maxSumTwoNoOverlap(A: 'List[int]', L: int, M: int):
    mapL = {}
    mapM = {}
    for i in range(len(A)-(L-1)):
        mapL[i] = sum(A[i:i+L])

    for i in range(len(A)-(M-1)):
        mapM[i] = sum(A[i:i+M])

    output = -float('inf')
    for k,v in mapL.items():
        for k1, v1 in mapM.items():
            #print(k,k1, v+v1)
            if k<=k1<=k+L-1 or k1<=k<=k1+M:
                pass
            else:
                output = max(output, v+v1)

    return output

print(maxSumTwoNoOverlap(A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2)) #20
print(maxSumTwoNoOverlap(A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2)) #29
print(maxSumTwoNoOverlap(A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3)) #31
print(maxSumTwoNoOverlap(A = [73,19,19,55,88,6,34,21,75,5,93,30,4,12,18,98,45,15,8,9,28,56,5,69,55,95,93,46,2,29,41,28,74,9,10,14,81,52,23,57,76,59,18,66,25,87,46,32,96,1]
, L = 26, M = 5)) #1537
print(maxSumTwoNoOverlap(A =[1,0,3],  L = 1, M = 2 )) #4





