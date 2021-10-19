class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n in {3**_ for _ in range(32) if 3**_ < 2**32}

# previous approach
# class Solution:
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         return  n>0 and 1162261467%n == 0