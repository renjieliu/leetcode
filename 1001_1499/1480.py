class Solution:
    def runningSum(self, nums: 'List[int]') -> 'List[int]':
        output = [nums.pop(0)]
        while nums:
            output.append(output[-1] + nums.pop(0))
        return output

