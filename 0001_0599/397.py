import math
def integerReplacement(n: int) -> int:
    cnt = 0
    while n>1:
        if n%2==0:
            n/=2
        else:
            if (int(math.log(n+1,2)) == math.log(n+1,2) or (n+1)%4 ==0) and n!=3: #if it can be divided by 4, it's the fastest, other than 3. as it can reach to 2 immediately.
                n +=1
            else:
                n -=1
        cnt +=1
    return cnt

print(integerReplacement(8))
print(integerReplacement(7))
print(integerReplacement(2134112345))


