def isPrime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, int(n**0.5)+1 ):
            if n%i == 0:
                return 0
    return 1


def sum_bits(n):
    return len(n) - len(n.replace("1",""))

def countPrimeSetBits(L, R):
    """
    :type L: int
    :type R: int
    :rtype: int
    """
    cnt = 0
    for i in range(L, R+1):
        if isPrime(sum_bits(str(bin(i)).replace("0b","")) ) == 1:
            cnt+=1

    return cnt

print(countPrimeSetBits(6,10)) #4
print(countPrimeSetBits(10,15)) #5
print(countPrimeSetBits(352527,357411)) #1473


