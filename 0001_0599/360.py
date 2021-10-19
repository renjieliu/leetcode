class Solution:
    def sortTransformedArray(self, nums: 'List[int]', a: int, b: int, c: int) -> 'List[int]':
        return sorted([a*x*x + b*x+c for x in nums])