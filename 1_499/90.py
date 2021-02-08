class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        def dfs(output, target, curr, rest):
            if len(curr) == target and sorted(curr) not in output:
                output.append(sorted(curr))
                return 0
            else:
                for i in range(len(rest)):
                    dfs(output, target, curr + [rest[i]], rest[i + 1:])

        output = [[]]
        i = 1
        while i <= len(nums):  # to control the cnt of the current arr
            for j in range(len(nums)):
                dfs(output, i, [nums[j]], nums[j + 1:])
            i += 1
        return output
