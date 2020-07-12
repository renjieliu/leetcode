class Solution:
    def rangeSum(self, nums: 'List[int]', n: int, left: int, right: int) -> int:
        arr = []
        mod = 10**9+7
        for i in range(len(nums)):
            arr.append(nums[i])
            for j in range(i+1, len(nums)):
                arr.append(arr[-1] + nums[j])
        return sum(sorted(arr)[left-1:right])%mod