class Solution:
    def maxSumAfterOperation(self, nums: 'List[int]') -> int:
        left = [0]
        right = [0]
        for i in range(1, len(nums)): #possible max from i-1 to leftmost
            left.append( max(nums[i-1], nums[i-1] + left[-1]))
        for i in range(len(nums)-2,-1, -1): #possible i+1 from rightmost
            right.append(max(nums[i+1], nums[i+1] + right[-1]))

        right = right[::-1] # reverse the right side array
        #print(left, right)
        output = 0
        for i in range(len(nums)): # check curr, curr+left, curr+right and curr+left+right
            curr = nums[i]**2
            output = max(output, curr, curr+left[i], curr+right[i], curr+left[i]+right[i])
        return output
