def isPalindrome(N):
    return str(N)==str(N)[::-1]

#for 10, it can form 101, and 1001.
def superpalindromesInRange(L: str, R: str) -> int:
    start = 1
    startLength = 1
    i = 1

    cnt  = 0
    while i<=100001: #this can guarantee the palindrome to be within the 10e18 range.
        if i**2>int(R):
            return cnt

        t = str(i)

        if len(t) == startLength:
            a = t+t[:-1][::-1] #this is to make sure a is a palindrome
            a1 = int(a) ** 2
            if isPalindrome(a1)  and int(L)<=a1 <= int(R):
                cnt += 1
            elif a1 > int(R):
                return cnt
        else:
            for j in range(start, i):
                x = str(j)
                b = x+x[:][::-1] #this is to make sure a is a palindrome
                b1 = int(b)**2
                if isPalindrome(b1) and int(L)<=b1 <= int(R):
                    cnt +=1
                elif b1 > int(R):
                    return cnt

            start = i
            startLength = len(t)
            i-=1

        i+=1
    return cnt

print(superpalindromesInRange('41241123', '10000231400000000')) #36
print(superpalindromesInRange("38455498359", '999999999999999999')) #45
print(superpalindromesInRange("9", '532')) #3
print(superpalindromesInRange("4", '1000')) #4
print(superpalindromesInRange("9357639525", '2353857225354')) #16


