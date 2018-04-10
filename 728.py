def is_selfDivide(num):
    output = 1
    temp = str(num)
    for i in range(0, len(temp)):
        if int(temp[i])==0:
            output = 0
            break
        else:
            if num%int(temp[i])==0:
                output = 1
            else:
                output = 0
                break
    return output

# print(is_selfDivide(10))

def selfDividingNumbers( left, right):
    output = list()
    for i in range(left, right+1):
        if is_selfDivide(i)==1:
            output.append(i)

    return output


print(selfDividingNumbers(1,22))