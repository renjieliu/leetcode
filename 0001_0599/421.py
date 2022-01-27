class Solution:
    def findMaximumXOR(self, nums: 'List[int]') -> int:  #RL 20220126 Read the solution, understand, and come up with own code
        m = max(nums).bit_length()
        output = 0
        for i in range(m, -1, -1): # from the highest bit, assuming I can find a^b matched to current assuming
            prefix = {n >> i for n in nums} #check for the current bit
            output <<= 1 #expand the output for 1 bit
            assuming = output|1 # assuming the current checking bit is 1
            output |= any(assuming^p in prefix for p in prefix) #for p in prefix, if curr^p is also in prefix
        return output 

    
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int: #RL 20220126 Read the solution, understand, and come up with own code
#         if len(nums)<2: return 0
#         maxBits = max(nums).bit_length()
#         output = 0
#         for i in range(maxBits, -1, -1): #from the highest to the lowest
#             prefix = {n >> i for n in nums} #
#             output <<= 1 #expand one bit with shift, the last digit is 0 for now.
#             curr = output | 1 # set the smallest bit to 1, assuming we can find a^b = curr
#             for p in prefix:  
#                 if curr^p in prefix:
#                     output |= 1  
#                     break
#         return output

    




# previous approach

# class Solution:
#     def findMaximumXOR(self, nums: 'List[int]') -> int:
#         if len(nums) < 2:
#             return 0
#         else:
#             def lkp(arr, curr, pre, lkp_set):  # to find if pre-length of arr element ^ curr is in the lkp_set
#                 for a in arr:
#                     temp = ""
#                     for i, c in enumerate(a[:pre]):
#                         temp += "1" if c != curr[i] else "0"
#                     if temp in lkp_set:
#                         return 1
#                 return 0

#             maxBits = len(bin(max(nums)).replace('0b', ''))  # maxBits
#             toBin = lambda x: bin(x).replace('0b', '')
#             arr = ['0' * (maxBits - len(toBin(n))) + toBin(n) for n in nums]  # turn to 0
#             output = ""
#             for i in range(maxBits):
#                 curr = output + "1"  # assume it can find n^curr in the array, else it will be 0
#                 lkp_set = {n[:i + 1] for n in arr}
#                 # print(lkp_set)
#                 if lkp(arr, curr, i + 1, lkp_set) == 1:
#                     output += "1"
#                 else:
#                     output += "0"

#             return int(output, 2)

