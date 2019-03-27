def nextGreaterElement(n: int) -> int:
    if len(str(n)) == 1:
        return -1

    tmp = str(n)
    found = 0
    replacePlace = None
    replaceBy = None

    for i in range(len(tmp) - 1, 0, -1):
        if tmp[i] > tmp[i-1]:
            replacePlace = i-1
            found = 1
            break

    if found ==0:
        return -1

    else:
        for i in range(len(tmp) - 1, 0, -1):
            if tmp[i] > tmp[replacePlace]:
                replaceBy = i
                break

    base = tmp[:replacePlace]+tmp[replaceBy]
    rest = sorted(tmp[replacePlace+1:replaceBy] + tmp[replacePlace] + tmp[replaceBy+1: ])
    return int(base+"".join(rest)) if int(base+"".join(rest))  <2**32 else -1


print(nextGreaterElement(12))
print(nextGreaterElement(21))
print(nextGreaterElement(987564321))
print(nextGreaterElement(230241)) # 230421 # 230412
print(nextGreaterElement(34123451))
print(nextGreaterElement(33333334))
print(nextGreaterElement(2147483647))
print(nextGreaterElement(9999999989))
print(nextGreaterElement(12443322)) #13222344 #13442322
print(nextGreaterElement(1999999999)) #13222344 #13442322