def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    prevTotal = 0
    dict = list()
    for i in range(1, 11):
        prevTotal += 9*(10**(i-1))*i
        dict.append( prevTotal)

    #print(dict)

    for v in dict:
        if v==n:
            return 9
        if v>n: #this to find the upper bound
            pos=dict.index(v)+1
            number = (( (10**pos)-1) - (v-n)//(pos)) # this is to find the number,  below is to determine which digit from the number to take
            check = str(number - 1)
            totalPos = int(dict[pos-1]) + (int(check) - (10**(pos))+1)*pos
            break

    return int(str(number)[0:n-totalPos][-1])


print(findNthDigit(11))
print(findNthDigit(10))
print(findNthDigit(1000))



