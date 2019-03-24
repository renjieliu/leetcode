def smallestRepunitDivByK(K: int):
    if int(str(K)[-1]) in [2, 4, 5, 6, 8, 0]:
        return -1
    elif K == 1:
        return 1
    else:
        temp = 11
        while temp%K != 0:
            temp = temp*10+1

        return len(str(temp))

print(smallestRepunitDivByK(1))
print(smallestRepunitDivByK(2))
print(smallestRepunitDivByK(19921))
print(smallestRepunitDivByK(73))
print(smallestRepunitDivByK(3))
print(smallestRepunitDivByK(7))
print(smallestRepunitDivByK(5))
print(smallestRepunitDivByK(9))
print(smallestRepunitDivByK(15))

