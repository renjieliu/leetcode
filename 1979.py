class Solution:
    def findGCD(self, nums: 'List[int]') -> int:
        a, b = min(nums), max(nums)
        while b!=0:
            a, b = b, a%b
        return a

