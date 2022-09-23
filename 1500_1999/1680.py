class Solution:
    def concatenatedBinary(self, n: int) -> int: # O( N | 1 )
        curr = ""
        for i in range(1, n+1): # go through from 1 to n, convert to binary, concatenate, and calc the result 
            curr += bin(i).replace('0b', '')
        return int(curr, 2) % (10**9+7)




# previous solution

# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         s = ""
#         for i in range(1, n+1):
#             s+= bin(i).replace('0b', '')
#         return int(s, 2) % (10**9+7)

# previous approach
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         mod = 10**9+7
#         s = ""
#         for i in range(1, n+1):
#             s+=bin(i).replace('0b','')
#         return int(s,2) % mod