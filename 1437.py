class Solution:
    def kLengthApart(self, nums: 'List[int]', k: int) -> bool:
        prev = -float('inf')
        for i, c in enumerate(nums):
            if c == 1:
                if i - prev > k:
                    prev = i
                else:
                    return False
        return True
