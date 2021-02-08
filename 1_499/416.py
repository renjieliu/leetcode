class Solution:
    def canPartition(self, nums: 'List[int]') -> bool:
        if len(nums) == 1 or sum(nums) %2 == 1 or max(nums) > sum(nums) // 2:
            return False
        else:
            target = sum(nums) // 2
            def dfs(curr, target, rem, arr, dp):
                if curr == target: # found
                    dp[curr] = True
                    return True
                elif curr in dp:
                    return dp[curr]

                else:
                    for i, a in enumerate(arr):
                        if a <= rem:
                            if dfs(curr+a, target, rem - a, arr[i+1:], dp ) == True:
                                dp[curr] = True
                                return dp[curr]
                            else:
                                dp[curr] = False
                    return False

        nums.sort()
        dp = {}
        return dfs(nums[0], target, target - nums[0], nums[1:], dp)
