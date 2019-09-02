def numPrimeArrangements(n: int):
    fact = lambda n: (n*fact(n-1)) if (n > 1) else (1 if n<=1 else n )

    # def fact(n):
    #     output = 1
    #     for i in range(1, n+1):
    #         output *= i
    #     return output

    def primeCnt(n):
        if n <=1:
            return 0
        output = 0
        for i in range(2,n+1):
            prime = 1
            for j in range(2,int(i**0.5)+1):
                if i %j == 0:
                    prime = 0
                    break
            if prime ==1:
                output+=1


        return output

    return (fact( n- primeCnt(n)) *  fact(primeCnt(n)) ) % (10**9 + 7)

print(numPrimeArrangements(100))
print(numPrimeArrangements(1))
print(numPrimeArrangements(12))
print(numPrimeArrangements(5))
print(numPrimeArrangements(77))

