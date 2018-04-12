def countPrimes(n):
    if n<3:
        return 0
    else:
        prime = [1]*n
        for i in range(2, int(n**0.5)+1 ):
            prime[i*i:n:i] = [0]*len(prime[i*i:n:i])

    return sum(prime)-2 #this is for prime[0] and prime[1]

print(countPrimes())

