def clumsy(N: int):
    cnt = 0
    output = ""
    operator = ""
    while N >0 :
        output += operator + str(N)
        cnt+=1
        if cnt%4==1:
            operator = "*"
        elif cnt%4 ==2:
            operator = "//"
        elif cnt %4 == 3:
            operator = "+"
        elif cnt%4 == 0:
            operator = "-"
        N-=1


    return eval(output)


print(clumsy(100))