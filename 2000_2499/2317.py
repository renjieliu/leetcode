class Solution:
    def maximumXOR(self, nums: 'List[int]') -> int: # O(N*K | N), K is the max bit length of n in nums
        one_loc = set()
        for n in nums: #record the bit loc with 1. 
            i = 0 
            while n > 0:
                if n % 2:
                    one_loc.add(i)
                n >>= 1 
                i+=1
                
        output = 0 
        for t in one_loc: #get the number with all = 1. xor with 0 to get all 1, which is the largest number
            output += 2**t
        return output
    
