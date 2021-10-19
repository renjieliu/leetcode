class Solution:
    def rearrangeArray(self, nums: 'List[int]') -> 'List[int]':
        nums.sort()
        output = []
        left = 0
        right = len(nums)-1
        while left<=right:
            output.append(nums[left]) #take the smallest
            left+=1
            if left<=right:
                output.append(nums[right]) # take the largest
                right-=1
        return output

