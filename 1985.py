class Solution:
    def kthLargestNumber(self, nums: 'List[str]', k: int) -> str:
        return str(sorted([int(_) for _ in nums], reverse = True)[k-1])


