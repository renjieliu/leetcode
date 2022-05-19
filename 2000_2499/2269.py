class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int: #O( N | 1)
        cnt = 0 
        s = str(num)
        for i in range(len(s)-k+1): #sliding window to compare each substring
            curr = s[i:i+k]
            cnt += 1 if int(curr) != 0 and num % int(curr) == 0 else 0
        return cnt

    
# previous solution

# class Solution:
#     def divisorSubstrings(self, num: int, k: int) -> int: #O( N | 1)
#         cnt = 0 
#         s = str(num)
#         for i in range(len(s)-k+1):
#             curr = s[i:i+k]
#             cnt += 1 if int(curr) != 0 and num % int(curr) == 0 else 0
#         return cnt

    
