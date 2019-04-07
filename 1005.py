def largestSumAfterKNegations(A: 'List[int]', K: int):
    b = A
    b.sort()
    sum = 0
    temp  = []
    for i in range(len(b)):
        left = K-(i+1)
        if i+1 <= K:
            if b[i]<0:
                temp.append(b[i]*-1)
            elif b[i] == 0:
                K = 0
            else:
                if i==0:
                    if left % 2 == 0:
                        temp.append(-b[i])
                    K=0
                else:
                    if left % 2 == 0:
                        if abs(b[i-1]) >= b[i]:
                            temp.append(-b[i])
                            K=0
                        else:
                            temp.pop()
                            temp.append(b[i-1])
                            temp.append(b[i])
                            K = 0
                    else:
                        temp.append(b[i])
                    K=0

        else:
            temp.append(b[i])


    for i in temp:
        sum+=i

    return sum


print(largestSumAfterKNegations([2,3,4],1))
print(largestSumAfterKNegations([3,-1,0,2],3))
print(largestSumAfterKNegations([2,-3,-1,5,-4],2))
print(largestSumAfterKNegations([-70,3, 9,9 ],2))
print(largestSumAfterKNegations([-70,3, 9,9 ],3))
print(largestSumAfterKNegations([-70,3, 9,9 ],4))
print(largestSumAfterKNegations([-2,9,9,8,4],5))
print(largestSumAfterKNegations([5,6,9,-3,3],2)) #20
print(largestSumAfterKNegations([-8,3,-5,-3,-5,-2],6)) #22



