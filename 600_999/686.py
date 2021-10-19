def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """

    if len(set(list(A)))<len(set(list(B))):
        return -1

    else:
        s1 = A
        s2 = B
        cnt = 1
        while s1.find(s2) == -1:
            cnt += 1
            if len(s1) > len(s2)*2 :
                cnt = -1
                break
            s1 = A * cnt
        return cnt

print(repeatedStringMatch("abcd", "cdabcdab"))
print(repeatedStringMatch("aaaa", "a"))
print(repeatedStringMatch("bb", "bbbbbbb"))
print(repeatedStringMatch("abababaaba", "aabaaba"))




