class Solution:
    def removePalindromeSub(self, s: str) -> int: #O(N | 1)
        return 1 + (s!=s[::-1]) #s only consists of a and b. so max 2 times, can clear out the whole string
    
# previous solution

# class Solution:
#     def removePalindromeSub(self, s: str) -> int:
#         return 0 if s == "" else (1 if s == s[::-1] else 2)

