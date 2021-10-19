def integerBreak(n: int):
    #the number can be break into 3^n. if the remaining is 1, then minus the mod by 1 and times 4.
    if n in (2,3):
        return n-1
    elif n%3==0:
        return 3**(n//3)
    elif n%3==1:
        return 3**((n//3)-1)*4
    elif n%3==2:
        return 3**(n//3)*2

print(integerBreak(10))
print(integerBreak(58))
print(integerBreak(2))
print(integerBreak(3))
print(integerBreak(4))