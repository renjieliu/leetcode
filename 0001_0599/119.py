def getRow(rowIndex: int) :
    r0 = [1]
    r1 = [1,1]

    if rowIndex ==0:
        return r0
    elif rowIndex ==1:
        return r1
    else:
        prev = r1
        for r in range(2, rowIndex+1):
            curr = []
            for c in range(0, r-1):
                curr.append(prev[c]+prev[c+1])


            prev = [1] + curr + [1]

    return prev

print(getRow(3))
print(getRow(4))
print(getRow(5))
print(getRow(6))