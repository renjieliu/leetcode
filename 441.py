def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    # cnt = 0
    #
    # while cnt*(cnt+1) <= 2*n:
    #     cnt+= 1

    # return cnt-1

    return int(((1+8*n)**0.5-1)/2) #https://zh.wikipedia.org/wiki/%E4%B8%80%E5%85%83%E4%BA%8C%E6%AC%A1%E6%96%B9%E7%A8%8B



print(arrangeCoins(8)) #3
print(arrangeCoins(5)) #2
print(arrangeCoins(10009)) #140
print(arrangeCoins(1)) #1
print(arrangeCoins(0)) #0



