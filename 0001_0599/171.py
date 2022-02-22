class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0  #treat it as a 26-base number
        for i in range(len(columnTitle)):
            c = columnTitle[-i-1]
            output += (ord(c)-ord('A')+1)*(26**i)
        return output
    


# previous approach

# class Solution:
#     def titleToNumber(self, s: str) -> int:
#         num = lambda x: ord(x) - 64
#         output = 0
#         i = 0
#         for c in s[::-1]:
#             output += num(c) * (26**i)
#             i+=1
#         return output


# Previous approach
# def titleToNumber(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     map = dict()
#     for i in range(65, 91):
#         map[chr(i)] = i-64
#     if len(s) == 1:
#         return map[s]
#     else:
#         pos = 1
#         sum = map[s[-1]]
#         for i in range(len(s)-1,0, -1):
#             sum += map[s[i]] * (26 ** pos)
#             pos+=1
#         return sum
#
# print(titleToNumber("AZZ"))
