def myPow(x: float, n: int):

    if n==0:
        return 1

    elif x in [0,1]:
        return x

    elif x==-1:
        return -1 if n%2 ==1 else 1


    elif n > 0:
        output = x
        for i in range(1,n):
            output *= x
            if abs(output) <0.00001:
                return 0
    elif n<0 :
        output = x
        for i in range(1, -n):
            output *= x
            if output > 100000:
                return 0
        output = 1/output

    return round(output,5)

print(myPow(2,10))
print(myPow(2.1,3))
print(myPow( 2.00000, -2))
print(myPow( 0, 0))