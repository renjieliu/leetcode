class Solution:
    def sortJumbled(self, mapping: 'List[int]', nums: 'List[int]') -> 'List[int]':
        def transform(n, mapping): # transform the number according to the mapping
            if n == 0: 
                return mapping[0]
            output = 0
            i = 0
            while n > 0:
                output += mapping[n%10] * (10**i) 
                n //= 10
                i+=1
            return output
        
        return sorted(nums, key = lambda x: transform(x, mapping)) # sort the nums by transformed number
    

