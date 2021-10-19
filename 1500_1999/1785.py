class Solution:
    def minElements(self, nums: 'List[int]', limit: int, goal: int) -> int:
        diff = abs(goal - sum(nums)) #check the difference, and see how many limit can be used to fill the gap
        return diff//limit + (1 if diff%limit else 0)

