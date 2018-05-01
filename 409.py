def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    len = 0
    max_odd = 0
    map = {}
    key = ""
    for i in s:
        if i in map:
            map[i]+=1
        else:
            map[i] = 1

    for k, v in map.items():
        if v%2==0:
            len+=v
        else:
            if v > max_odd:
                max_odd = v
                key = k

    for k, v in map.items():
        if v%2 != 0:
            if key == k:
                len += v
            else:
                len +=v-1
    return len

print(longestPalindrome("abccccdd"))
print(longestPalindrome("absdfasfasdfcccd"))
print(longestPalindrome("absdfaasssdfasdfsafasfsdfsafdsfasdfcccd"))


