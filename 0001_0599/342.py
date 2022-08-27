class Solution:
    def isPowerOfFour(self, n: int) -> bool: # O( 1 | 1 )
        return n > 0 and n.bit_length() % 2 == 1 and n & (n-1) == 0 # n needs to be positive, n needs to be 2x+1 length, , and all the bits need to be 0, except for the first bit.
    
    
    

# previous solution

# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:
#         b = bin(num)
#         b_strip = b.rstrip('0')
#         return num ==1 or (len(b_strip) ==3  and  len(b_strip) < len(b) and (len(b)-len(b_strip))%2 == 0)


# previous solution

# class Solution:
#     def isPowerOfFour(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         dict = list()       
        
#         for i in range(0, 32):
#             if 4**i<2**31:
#                 dict.append(4**i)
#             else:
#                 break

#         return True if num in dict else False


