class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & n-1 == 0
        # while n > 1:
        #     if n % 2:
        #         return False
        #     else:
        #         n = n >> 1
        # return True

        


# previous approach
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return True if n > 0 and n & n - 1 == 0 else False

#approach 3

        # return True if n>0 and str(bin(n)).count('1') ==1 else False


# approach 2
#         e = 1000
#         s = 0
#         while s<=e:
#             mid  = (s+e)//2
#             if 2**mid == n :
#                 return True
#             else:
#                 if 2**mid>n:
#                     e = mid - 1
#                 else:
#                     s = mid +1
#         return False

# approach 1
#         i = 0
#         while True:
#             if 2**i < n :
#                 i+=1
#             elif 2**i == n:
#                 return True
#             else:
#                 return False

