class Solution:
    def countDistinctIntegers(self, nums: 'List[int]') -> int: # O( N | N )
        return len(set(nums) | set(int(str(n)[::-1]) for n in nums)) # the original set, and the one with each number reversed
    
