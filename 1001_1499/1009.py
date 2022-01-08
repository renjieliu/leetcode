class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if n == 0 else n ^ 2**n.bit_length() - 1
    
 

# previous approach
# class Solution:
#     def bitwiseComplement(self, n: int) -> int:
#         if n == 0:
#             return 1 
#         res = 0 
#         power = 0 
#         while n >= 1: # if n % 2, then add 0 to the res, else, 2**power
#             res += 0 if n % 2 else 2**power
#             n = n >> 1
#             power += 1
#         return res


# previous approach
# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         digits = 0
#         n = N
#         while n > 0: #find the 1111 to be Xor'ed
#             digits +=1
#             n = n >> 1
#         return 1 if N == 0 else N ^ (2**digits-1)

