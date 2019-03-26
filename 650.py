def isPrime(n):
    if n in [1,2]:
        return 1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

def minSteps(n: int):
    if n==1:
        return 0
    elif n ==2 :
        return 2
    else:
        if isPrime(n):
            return n
        temp = 1
        operation = 1 #this is the initial copy
        keepAdding = 1
        cnt = 0
        while temp<=n: #keep adding temp+original lenfth, if currentnumber can be divided by n, then replace temp with currentnumber.
            if n%temp == 0:
                cnt = temp
                keepAdding =0
                temp += cnt
                operation+=2
            elif keepAdding ==0 and n%temp !=0:
                temp += cnt
                operation+=1

            elif n%temp !=0 and keepAdding ==1:
                temp+=1
                operation+=1

            if temp==n:
                return operation -1 #this is to minus current operation.

print(minSteps(3)) #3
print(minSteps(8)) #6
print(minSteps(10)) #7
print(minSteps(12)) #7
print(minSteps(18)) #8
print(minSteps(24)) #8
print(minSteps(22)) #8
print(minSteps(999)) #46
print(minSteps(258)) #48



