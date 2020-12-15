class Solution:
    def sortedSquares(self, nums: 'List[int]') -> 'List[int]':
        l, r = 0, len(nums)-1
        output = []
        while l <= r:
            output.append(max(nums[l]**2, nums[r]**2))
            if output[-1]==nums[l]**2:
                l += 1
            else:
                r -= 1
        return output[::-1]

# previous approach
# class Solution:
#     def sortedSquares(self, nums: 'List[int]') -> 'List[int]':
#         return sorted([n**2 for n in nums])
#
#

