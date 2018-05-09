def guess(num):
    n = 6
    if num == n:
        return 0
    elif num > n:
        return -1
    elif num<n:
        return 1




# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """
    k = n
    end = n
    start = 1
    while guess(k)!= 0:
        if guess(k) ==-1:
            end = k
            k = (start+end)//2
        elif guess(k) == 1 :
            start = k
            k = (start+end)//2

    else:
        return k


print(guessNumber(10))




