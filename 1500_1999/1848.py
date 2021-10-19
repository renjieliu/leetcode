class Solution:
    def getMinDistance(self, nums: 'List[int]', target: int, start: int) -> int:
        output = float('inf')
        for i, n in enumerate(nums):
            if n == target:
                output = min(abs(i-start), output)
        return output


