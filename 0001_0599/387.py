class Solution:
    def firstUniqChar(self, s: str) -> int: # O( N | 26 )
        loc = [float('inf')] * 26 #initialze the count of each letter as float('inf')
        for i, c in enumerate(s):
            loc[ord(c) - ord('a')] = len(s) if loc[ord(c) - ord('a')] != float('inf') else i #if it's seen before,  set the value to len(s), otherwise, set it to index i
        return -1 if min(loc) == len(s) else min(loc) #for the letter met more than once, it will be len(s). 
    



# previous solution

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         hmp = {}
#         for i,c in enumerate(s):
#             if c not in hmp:
#                 hmp[c] = []
#             hmp[c].append(i)
#         output = []
#         for v in hmp.values():
#             if len(v) ==1:
#                 output += v
#         output.sort()
#         return -1 if len(output) ==0 else output[0]




# previous solution

# class Solution:
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         for i in range(0, len(s)):
#             if (s[0:i] + s[i+1:]).find(s[i])  == -1:
#                 return i

#         return -1

