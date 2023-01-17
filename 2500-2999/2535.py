class Solution:
    def differenceOfSum(self, nums: 'List[int]') -> int: # O( NlogN | 1 )
        total = sum(nums)
        def calc(n): # calculate the sum of digits in n
            output = 0  
            while n > 0:
                output += n % 10
                n //=10
            return output
    
        return abs(total - sum(calc(_) for _ in nums))
    

