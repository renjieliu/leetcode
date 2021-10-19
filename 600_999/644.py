class Solution:
    def findMaxAverage(self, nums: 'List[int]', k: int) -> float:
        n = len(nums)
        temp_prefixsum = [0 for _ in range(n + 1)]
        for i in range(n):
            temp_prefixsum[i + 1] = temp_prefixsum[i] + nums[i]

        left, right = min(nums), max(nums)

        def isvalid(temp_prefixsum, mid):
            minval = float("inf")
            for i in range(n + 1 - k):
                minval = min(minval, temp_prefixsum[i] - i * mid)
                if temp_prefixsum[i + k] - (i + k) * mid >= minval:
                    return True
            return False

        while right - left > 0.00001:
            mid = (left + right) / 2

            if isvalid(temp_prefixsum, mid):
                left = mid
            else:
                right = mid

        return left