class Solution:
    def maxPower(self, s: str) -> int:
        output = 1 
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                curr = 1
            output = max(curr, output)
        return output
    


# previous approach
# class Solution:
#     def maxPower(self, s: str) -> int:
#         if s == "":
#             return 0
#         output = 1
#         curr = 1
#         for i in range(1, len(s)):
#             if s[i] == s[i - 1]:
#                 curr += 1
#             else:
#                 curr = 1

#             output = max(curr, output)

#         return output


# previous approach
# class Solution:
#     def maxPower(self, s: str) -> int: 
#         currStart = 0
#         output = 1
#         i = 1
#         while i < len(s):
#             if s[i] != s[i-1]:
#                 output = max(output, i-currStart)
#                 currStart = i
#             i+=1
#         output = max(output, i-currStart)
#         return output


