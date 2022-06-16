class Solution:
    def longestPalindrome(self, s: str) -> str: # O( N**2 | N**2 )
        n = len(s) 
        output_start = 0 
        L = 1
        dp = [[0] * n for _ in s] #r, c means the index start, end for s
        
        for i in range(n): # diagonal should be 1 for each character
            dp[i][i] = 1
        
        for end in range(n):
            for start in range(end-1, -1, -1):
                if s[start] == s[end] and (end-start == 1 or dp[start+1][end-1] == 1 ): # "baab", start+1 is a , end -1 is a 
                    dp[start][end] = 1
                    if end - start + 1 > L:
                        L = end-start+1
                        output_start = start
        
        return s[output_start: output_start+L]
                    

        
        
# class Solution:
#     def longestPalindrome(self, s: str) -> str: #O(N**2 | 1)
#         n = len(s)
#         start = 0 
#         L = 1 #the length of the longest palindromic substring
        
#         for i in range(n): #go through each character, and expand from current character, left and right
#             right = i  
#             while right < n and s[right] == s[i]:  #aaa 
#                 right += 1 
            
#             left = i - 1
#             while left > -1 and right < n and s[left] == s[right]: # bbaaabb
#                 left -= 1
#                 right += 1
            
#             X = (right - 1) - (left + 1) + 1 #current palindromic substring length
            
#             if X > L: 
#                 L = X
#                 start = left + 1
        
#         return s[start: start+L]
                




# previous solution

# class Solution:
#     def longestPalindrome(self, s: str) -> str: # O( N**2 | N**2 )
#         n = len(s) 
#         output_start = 0 
#         L = 1
#         dp = [[0] * n for _ in s] #r, c means the index start, end for s
        
#         for i in range(n): # diagonal should be 1 for each character
#             dp[i][i] = 1
        
#         for end in range(n):
#             for start in range(end-1, -1, -1):
#                 if s[start] == s[end] and (end-start+1 == 1 or dp[start+1][end-1] == 1 ): # "baab", start+1 is a , end -1 is a 
#                     dp[start][end] = 1
#                     if end - start + 1 > L:
#                         L = end-start+1
#                         output_start = start
        
#         return s[output_start: output_start+L]
                    



# previous solution

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1: return s
#         output = ""
#         for i in range(len(s)) :
#             for j in range(len(s), i, -1):
#                 curr = s[i:j]
#                 if len(curr) <= len(output):
#                     break
#                 elif curr == curr[::-1]:
#                     if len(curr) > len(output):
#                         output = curr
#         return output
