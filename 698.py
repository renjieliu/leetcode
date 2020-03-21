class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: int) -> bool:
        def dfs(k, arr, pos, target, curr, check):
            if k == 1:
                return True
            else:
                if curr == target:
                    return dfs(k - 1, arr, 0, target, 0, check)
                else:
                    for i in range(pos, len(arr)):
                        if check[i] == 0:
                            check[i] = 1
                            if dfs(k, arr, i, target, curr + arr[i], check) == True:
                                return True
                            else:
                                check[i] = 0
                return False

        s = sum(nums)
        if k == 0 or s % k != 0: return False
        target = s // k
        return dfs(k, nums, 0, target, 0, [0] * len(nums))

