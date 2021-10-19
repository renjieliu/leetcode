class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = palindrome
        for i, c in enumerate(s):
            t = s[:i] + 'a' + s[i+1:]
            if t != t[::-1]:
                return t
        return "" if len(s) <= 1 else s[:-1]+'b'


# previous approach
# class Solution:
#     def breakPalindrome(self, palindrome: str) -> str:
#         s = palindrome
#         ifNotPalin = lambda x: True if x != x[::-1] else False
#         for i in range(len(s)): #replace from left to right - with ascii lower than curr
#             c = s[i]
#             for j in range(ord('a'), ord(c)):
#                 tmp = s[:i] + chr(j) + s[i+1:]
#                 if ifNotPalin(tmp):
#                     return tmp
#
#         for i in range(len(s)-1, -1, -1): #replace from right to left, with ascii higher than curr
#             c = s[i]
#             for j in range(ord(c), ord('z')+1):
#                 tmp = s[:i] + chr(j) + s[i+1:]
#                 if ifNotPalin(tmp):
#                     return tmp
#
#         return ""



# previous approach
# class Solution:
#     def breakPalindrome(self, palindrome: str) -> str:
#         if len(palindrome) == 1:
#             return ""
#         i = 0
#         while i < len(palindrome):
#             t = palindrome[:i] + 'a' + palindrome[i + 1:]  # replace current to 'a'
#             if t != t[::-1]:  # still palindrome, need to continue
#                 return t
#             i += 1
#         return palindrome[:-1] + 'b'
#
#
