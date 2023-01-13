class Solution:
    def maximumCount(self, nums: 'List[int]') -> int: # O( N | 1 )
        A = B = 0
        for n in nums: # count the positive and negative numbers in the num
            A += n > 0 
            B += n < 0 
        return max(A, B)
    




