def isGood(n):
    dict  = [1,5,-1,-1,2,9,-1,8,6,0]
    output = ""
    lst = list(str(n))
    for i in lst:
        if dict[int(i)-1] == -1:
            return 0
        else:
            output+=str(dict[int(i)-1])
    if int(output) == n:
        return 0
    else:
        return 1

def rotatedDigits(N):
    """
    :type N: int
    :rtype: int
    """
    cnt = 0
    for i in range(1, N+1):
        if isGood(i):
            cnt += 1
    return cnt

print(rotatedDigits(180))

