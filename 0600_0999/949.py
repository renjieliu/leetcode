def largestTimeFromDigits(A: 'List[int]'):
    A = [str(i) for i in A]
    check = []
    for hour in range(0,24):
        hour = '0' + str(hour) if hour<10 else str(hour)
        for min in range(0,60):
            min = '0' + str(min) if min<10 else str(min)
            check.append(hour+min)


    for j in range(len(check)-1, -1, -1 ):
        curr = check[j]
        if sorted(curr) == sorted(A):
            return curr[:2]+ ":" + curr[2:]

    return ""

print(largestTimeFromDigits([1,2,3,4]))
print(largestTimeFromDigits([5,5,5,5]))





