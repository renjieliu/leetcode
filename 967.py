def numsSameConsecDiff(N, K):
    #N - digits
    #K - diff
    temp =[0,1,2,3,4,5,6,7,8,9]
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
            if cal_minus >=0:
                temp.append( str(curr) + str(cal_minus) )

            iter+=1

       # print(temp)

        width+=1

    for i in temp:
        if len(str(int(i)))== N:
            output.append(int(i))

    return list(set(output))

print( numsSameConsecDiff(3,3))
print( numsSameConsecDiff(9,1))
print( numsSameConsecDiff(3,7))