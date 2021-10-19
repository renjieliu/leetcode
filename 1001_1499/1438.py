class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minStk = [] #store the minValue loc, increasing
        maxStk = [] #store the maxValue loc, decreasing 
        left = 0
        curr = 0 
        output = 0
        for curr in range(len(nums)):
            while minStk and nums[curr] < minStk[-1]:
                minStk.pop()
            while maxStk and nums[curr] > maxStk[-1]:
                maxStk.pop()
            minStk.append(nums[curr])
            maxStk.append(nums[curr])
            
            while maxStk[0] - minStk[0]> limit: # just need to compare the max and min value in the current window
                if nums[left] == maxStk[0]:
                    maxStk.pop(0)
                if nums[left] == minStk[0]:
                    minStk.pop(0)
                left +=1 
                
            output = max(output, curr-left+1)
        return output
