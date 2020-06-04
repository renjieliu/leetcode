class Solution:
    def reverseString(self, s: 'List[str]') -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):  # in-place swap
            t = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = t

# OLD solution, not optimal
# def reverseString(s):
#     output = ""
#     for i in range(len(s)-1, -1,-1):
#         output += s[i]
#     return  output
#
# print(reverseString("Hello"))