# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version < 2:
        return False
    else:
        return True

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    start = 1
    end = n

    now_1 = (start + end) // 2
    now_2 = (start + end) // 2 + 1

    while isBadVersion(now_1) == isBadVersion(now_2):
        if now_1 == 1:
            return 1
        elif isBadVersion(now_1) : #both are bad version, need to move behind
            end = now_1
        else:  #both are good version, need to move behind
            start = now_2
        now_1 = (start + end) // 2
        now_2 = (start + end) // 2+1

    else:
        if isBadVersion(now_1):
            return now_1
        else:
            return now_1 + 1

print(firstBadVersion(4))




