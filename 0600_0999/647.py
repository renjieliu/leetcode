class Solution:
    def countSubstrings(self, s: str) -> int: #O(N3 | 1)
        cnt = 0 
        for i in range(len(s)): #check each substring, and see if it's palindromic
            for j in range(i+1, len(s)+1):
                cnt += 1 if s[i:j] == s[i:j][::-1] else 0
        return cnt
    


# previous solution

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         cnt = len(s)
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 cnt += 1 if s[i:j+1] == s[i:j+1][::-1] else 0
#         return cnt



# previous solution 

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         cnt = 0
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                  cnt += (1 if s[i:j] == s[j:i:-1] else 0)

#         return cnt
