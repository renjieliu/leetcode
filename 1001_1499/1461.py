class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool: #O(N | N)
        seen = set() #store all the distinct substring
        for i in range(len(s)+1-k):
            seen.add(s[i:i+k])
        return len(seen) >= 2**k #to check if the total distinct substring is >= 2**k possibilities
    

# previous solution

# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         lkp = set()
#         for i in range(len(s)+1-k):
#             lkp.add(s[i:i+k])
#         return len(lkp) == 2**k


