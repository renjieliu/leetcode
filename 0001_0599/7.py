def func(self, num):
    neg = 1
    if str(num)[0] =="-":
        neg = -1
    temp = ""
    for i in range(len(str(num))-1,-1,-1):
        if str(num)[i] == "-":
            neg = -1
        else:
            temp += str(num)[i]

    if int(temp) >= 2**31 or int(temp) < -1*(2**31):
        neg = 0

    return int(temp) * neg

print(func(120))

