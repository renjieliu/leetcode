def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    sum_s = 0
    for i in list(s):
        sum_s += ord(i)

    sum_t=0
    for i in list(t):
        sum_t += ord(i)

    return chr(sum_t - sum_s)

print(findTheDifference("abcd", "abcde"))





