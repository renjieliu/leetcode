def isPalindrome(s:'str'):
    if len(s) == 1 :
        return 1
    else:
        if len(s)%2==0:
            return 1 if s[:len(s)//2] == s[len(s)//2:][::-1] else 0
        else:
            return 1 if s[:len(s)//2] == s[len(s)//2+1:][::-1] else 0


def longestPalindrome(s: 'str'):
    if len(s) == 1:
        return s
    else:
        temp = ""
        max = 0
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if isPalindrome(s[i:j+1]) == 1:
                    if len(s[i:j+1]) > max:
                        temp = s[i:j+1]
                        max = len(s[i:j+1])
                    break  # since this is from whole to single approach, there will not be any longer Palindrome for current i

        return temp
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("aa"))


