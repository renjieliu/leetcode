class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        def combo(output, curr, target, arr):
            if len(curr) == target:
                output.append(curr)
            else:
                for i in range(len(arr)):
                    combo(output, curr+[arr[i]], target, arr[i+1:])
        output = [[]]
        for k in range(1, len(nums)+1):
            for i, n in enumerate(nums):
                combo(output, [n], k, nums[i+1:])
        return output