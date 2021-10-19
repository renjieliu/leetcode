class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def helper(a, b): #this is to find the longest common sequence of a and b 
            dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1) ]
            for r in range(1, len(a)+1):
                for c in range(1, len(b)+1):
                    curr = dp[r-1][c-1] + (a[r-1] == b[c-1])
                    dp[r][c] = max(curr, dp[r-1][c], dp[r][c-1])
            return dp[-1][-1]
        
        return (len(s) - helper(s, s[::-1]) ) <= k
                    

# previous approach
# class Solution:
#     def isValidPalindrome(self, s: str, k: int) -> bool:
#         def lcs(a, b): #to find the longest common sequence of a and b
#             dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
#             for r in range(1, len(a)+1):
#                 for c in range(1, len(b)+1):
#                     dp[r][c] = max(dp[r-1][c-1] + (a[r-1] == b[c-1]), dp[r][c-1], dp[r-1][c])
#             return dp[-1][-1]
#         return len(s) - lcs(s, s[::-1]) <= k

