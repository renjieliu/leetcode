class Solution:
    def maxFrequency(self, nums: 'List[int]', k: int) -> int:
        if len(nums) == 1: return 1
        nums.sort()
        curr = l = r = 0
        output = 1
        while r < len(nums):
            curr += nums[r]
            diff = nums[r] * (r-l+1) - curr #sum of the current window, if all the numbers are the largest one, minus actual
            if diff <=k:
                output = max(output, r-l+1)
            else:
                while l < r and  diff > k: #shrink the window...
                    curr -= nums[l]
                    l+=1
                    diff = nums[r] * (r-l+1) - curr
                output = max(output, r-l+1)
            r+=1
        return output


