class Solution:
    def separateDigits(self, nums: 'List[int]') -> 'List[int]': # O( NlogN | NlogN )
        def helper(n):# get each digit in n
            output = []
            while n > 0:
                output.append(n % 10) 
                n //= 10
            return output[::-1] # reverse the output order

        res = []
        for n in nums:
            res += helper(n)
        return res




