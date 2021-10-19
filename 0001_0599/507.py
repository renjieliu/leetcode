def checkPerfectNumber(num):
    sum = 0
    if num <= 1:
        return False
    else:
        for i in range(1, int(num**0.5+1)):
            sum += i if num % i == 0 else 0
            sum += num / i if num % i == 0 and i!=1 else 0
        if sum==num:
            return True
        else:
            return False


print(checkPerfectNumber(28))