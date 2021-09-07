class Solution:
    def romanToInt(self, s: str) -> int:
        hmp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        i = 0
        while i < len(s) - 1:
            curr = s[i]
            nxt = s[i + 1]
            if hmp[curr] < hmp[nxt]:
                output += (hmp[nxt] - hmp[curr])
                i += 2
            else:
                output += hmp[curr]
                i += 1

        if i == len(s) - 1:  # it reach the last character, which means the last batch is not 2 characters
            output += hmp[s[-1]]
        return output

# previous approach
# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     map = {
#         "I": 1
#         , "V": 5
#         , "X": 10
#         , "L": 50
#         , "C": 100
#         , "D": 500
#         , "M": 1000
#     }
#     pos = 0
#     output = 0
#
#     while pos<len(s)-1:
#         if s[pos]=="I" and s[pos+1] == "V":
#             output+=4
#             pos+=2
#
#         elif s[pos]=="I" and s[pos+1] == "X":
#             output+=9
#             pos+=2
#         elif s[pos] == "X" and s[pos + 1] == "L":
#             output += 40
#             pos += 2
#         elif s[pos] == "X" and s[pos + 1] == "C":
#             output += 90
#             pos += 2
#
#         elif s[pos] == "C" and s[pos + 1] == "D":
#             output += 400
#             pos += 2
#
#         elif s[pos] == "C" and s[pos + 1] == "M":
#             output += 900
#             pos += 2
#         else:
#             output+= map[s[pos]]
#             pos+=1
#
#     return output + (map[s[-1]] if pos == len(s)-1 else 0 )
#
# print(romanToInt("III"))
# print(romanToInt("IV"))
# print(romanToInt("IX"))
# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))
# print(romanToInt("MDCXCV"))
#
#
#
#
#
#
#
#
#
#
#
