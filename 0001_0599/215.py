class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        return sorted(list(nums), reverse = True)[k-1]