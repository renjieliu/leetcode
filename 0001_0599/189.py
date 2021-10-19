class Solution:
    def rotate(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = k % len(nums)
        nums[:] = nums[-pivot:] + nums[:-pivot]

# previous approach
# def rotate(nums, k):
#     return nums[len(nums)-k:len(nums)] + nums[0:len(nums)-k]
# print(rotate([1,2],1))





