class Solution:
    def isPowerOfThree(self, n: int) -> bool: # O( 1 | 1 )
        return n > 0 and 3**20 % n == 0 # 20 is any arbitrary number, as long as it's 3**x is larger than the max



# previous solution

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool: # O( logN | logN )
#         lkp = {3**_ for _ in range(100) if 3**_ <= n} # build a look up set for all the power of 3 within requirement
#         return n in lkp



# previous solution

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return n in {3**_ for _ in range(32) if 3**_ < 2**32}

# # previous approach
# # class Solution:
# #     def isPowerOfThree(self, n):
# #         """
# #         :type n: int
# #         :rtype: bool
# #         """
# #         return  n>0 and 1162261467%n == 0