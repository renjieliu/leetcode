def canThreePartsEqualSum(A: 'List[int]'):
    total = sum(A)
    if total%3 !=0:
        return False
    curr_sum = 0
    for i in range(len(A)):
        curr_sum+=A[i]
        if curr_sum == total//3:
            curr_sum2=0
            for j in range(i+1, len(A)):
                curr_sum2 += A[j]
                if curr_sum2 == total//3:
                    if sum(A[j+1:]) == curr_sum2:
                        return True
    return False





print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))