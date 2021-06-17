class Solution:
    def numSubarrayBoundedMax(self, nums: 'List[int]', left: int, right: int) -> int:
        l = r = 0
        badConti = 0
        cnt = 0
        while r < len(nums):
            if nums[r] < left:
                badConti += 1  #the continuous bad items , < left
            else:
                badConti = 0 # reset the bad
                if nums[r] > right: # move the left to the next item
                    l = r+1
            cnt += r-l+1 #total item - bad continious is the result
            cnt -= badConti
            r+=1
        return cnt

# previous approach
# class Solution:
#     def numSubarrayBoundedMax(self, nums: 'List[int]', left: int, right: int) -> int:
#         def contiValid(arr, v): # count the continuous value <= v
#             output = curr = 0
#             for a in arr:
#                 curr = curr+1 if a <=v else 0
#                 output+=curr
#             return output
#         return contiValid(nums, right) - contiValid(nums, left-1)
#
