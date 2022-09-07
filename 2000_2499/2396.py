class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool: # O( 1 | 1 )
        return False # n-2 base will always be 12, therefore, the result is always false
    


# previous approach

# class Solution:
#     def isStrictlyPalindromic(self, n: int) -> bool: # O( 1 | 1 )
#         return False # n-2 base will always be 12, therefore, the result is always be false
    

# previous approach

# class Solution:
#     def isStrictlyPalindromic(self, n: int) -> bool: # O( NlogN | 1 )
#         def cast(v, base): #cast v to base
#             output = ""
#             while v > 0:
#                 output = str(v%base) + output
#                 v //= base
#             return output
        
#         for base in range(2, n-1): #cast all the numbers to different base, and check if it's palindromic
#             t = cast(n, base)
#             if t != t[::-1]:
#                 return False
#         return True
    
