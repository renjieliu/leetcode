def numsSameConsecDiff(N, K):
    #N - digits
    #K - diff
    temp = [str(_) for _ in range(10)]
    output = []
    width = 1
    iter = 0
    while width < N:
        length = len(temp)
        while iter < length:
            curr = temp[iter]
            cal_add = int(str(curr)[-1])+K
            if cal_add <10:
                temp.append ( str(curr) + str(cal_add))
            cal_minus = int(str(curr)[-1])-K
            if cal_minus >=0 and cal_minus!=cal_add:
                temp.append( str(curr) + str(cal_minus) )

            iter+=1

       # print(temp)

        width+=1

    for i in temp:
        o = int(i)
        if len(str(o))== N:
            output.append(o)

    return output

print( numsSameConsecDiff(3,3))
print( numsSameConsecDiff(9,1))
print( numsSameConsecDiff(3,7))
print( numsSameConsecDiff(3,0))
print( numsSameConsecDiff(1,0))