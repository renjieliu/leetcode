class Solution:
    def triangleNumber(self, nums: 'List[int]') -> int:
        nums.sort()
        output = 0
        for i in range(len(nums)-1, -1, -1):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    output += right - left
                    right-= 1
                else:
                    left += 1
        return output


# previous approach
# class Solution:
#     def triangleNumber(self, nums: 'List[int]') -> int:
#         nums.sort()
#         output=0
#         #set the 3rd edge as i, and use the other 2 to iterate through the whole array
#         for i in range(len(nums)-1,-1, -1):
#             edge_1 = 0
#             edge_2 = i-1
#             while edge_1 < edge_2:
#                 if nums[edge_1]+nums[edge_2]>nums[i]:
#                     output+=edge_2 - edge_1
#                     edge_2-=1
#                 else:
#                     edge_1+=1
#         return output

