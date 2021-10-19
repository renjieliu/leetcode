class Solution:
    def canBeIncreasing(self, nums: 'List[int]') -> bool:
        def valid(arr):
            if len(arr) <= 1:
                return True
            else:
                for i in range(1, len(arr)):
                    if arr[i] <= arr[i-1]:
                        return False
                return True
        l = len(nums)
        cnt = 0
        for i in range(1, l):
            if nums[i] <= nums[i-1]:
                return valid(nums[:i-1] + nums[i:]) or valid(nums[:i] + nums[i+1:])
        return True

