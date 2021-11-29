class Solution:
    def targetIndices(self, nums: 'List[int]', target: int) -> 'List[int]':
        return [i for i, c in enumerate(sorted(nums)) if c == target]
    
