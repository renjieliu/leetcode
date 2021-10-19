class Solution:
    def createTargetArray(self, nums: 'List[int]', index: 'List[int]') -> 'List[int]':
        output = []
        for i in range(len(nums)):
            output = output[:index[i]] + [nums[i]] + output[index[i]:]
        return output