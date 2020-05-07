class Solution:
    def longestSubarray(self, nums: 'List[int]', limit: int) -> int:
        minStk = []  # store the minValue loc, increasing
        maxStk = []  # store the maxValue loc, decreasing
        left = 0
        curr = 0
        output = 0
        while curr < len(nums):
            while minStk and nums[curr] <= nums[minStk[-1]]:
                minStk.pop()
            while maxStk and nums[curr] >= nums[maxStk[-1]]:
                maxStk.pop()
            minStk.append(curr)
            maxStk.append(curr)

            if nums[maxStk[0]] - nums[minStk[0]] > limit:  # just need to compare the max and min value in the current window
                left += 1  # max(maxStk[0]+1,minStk[0]+1)
                while left > maxStk[0]:
                    maxStk.pop(0)
                while left > minStk[0]:
                    minStk.pop(0)

            output = max(output, curr - left + 1)
            curr += 1
            print(left, curr)
        return output