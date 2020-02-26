class Solution:
    def makesquare(self, nums: 'List[int]') -> bool:
        def dfs(taken, target, group_cnt, nums, curr, pos):
            if group_cnt == 4:
                return 1
            elif curr == target:
                return dfs(taken, target, group_cnt + 1, nums, 0, 0)
            else:
                for i in range(pos, len(nums)):
                    if taken[i] == 0 and curr + nums[i] <= target:
                        taken[i] = 1
                        if dfs(taken, target, group_cnt, nums, curr + nums[i], i + 1) == 1:
                            return 1
                        else:
                            taken[i] = 0
                return 0

        s = sum(nums)
        nums.sort()
        if len(nums) < 4 or s == 0 or s / 4 != s // 4 or nums[-1] > s // 4:
            return False
        else:
            target = s // 4
            taken = [0] * len(nums)  # to label if each pos has been taken
            group_cnt = 1
            curr = 0
            pos = 0
            if dfs(taken, target, group_cnt, nums, curr, pos) == 1:
                return True
            else:
                return False
