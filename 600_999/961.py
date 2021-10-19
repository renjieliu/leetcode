def repeatedNTimes(A: 'List[int]'):
    list = []
    for i in A:
        if i not in list:
            list.append(i)
        else:
            return i

print(repeatedNTimes([5,1,5,2,5,3,5,4]))
