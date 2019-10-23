def longestOnes(A: 'List[int]', K: int):
    l = 0
    output = 0
    pos_0 = []
    s = 0
    for r in range(len(A)):
        if A[r] == 0 and K != 0:
            if len(pos_0) == K:
                output = max(output, s)
                l = pos_0[0]
                s = (r - l)  # current range sum
                pos_0.pop(0)
                pos_0.append(r)
            else:
                pos_0.append(r)
                s += 1

        elif A[r] == 0 and K == 0:
            output = max(output, s)
            s = 0

        else:
            s += 1
        # print(output)
    return max(output, s)


print(longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], K = 2)) #6
print(longestOnes(A = [1,1,1], K = 2)) #3
print(longestOnes(A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3)) #10
print(longestOnes(A = [0,0,1,1,1,0,0], K=0)) #3
print(longestOnes(A = [0,0,0,1], K=4)) #4
print(longestOnes([1,1,1,0,0,0,1,1,1,1], 0 )) #4






