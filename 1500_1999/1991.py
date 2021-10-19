class Solution:
    def findMiddleIndex(self, nums: 'List[int]') -> int:
        arr_left = [0]
        for n in range(1, len(nums)):
            arr_left.append(arr_left[-1] + nums[n - 1])
        arr_right = [0]
        for n in range(len(nums) - 2, -1, -1):
            arr_right.append(arr_right[-1] + nums[n + 1])
        arr_right = arr_right[::-1]
        for i in range(len(nums)):
            if arr_left[i] == arr_right[i]:
                return i
        return -1
