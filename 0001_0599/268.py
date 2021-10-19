class Solution:
    def missingNumber(self, nums: 'List[int]') -> int:
        output = len(nums)
        for i, n in enumerate(nums): #i^n should be 0, if both loc and number exist in the array, the array doesn't have to be sorted
            output ^= i^n
        return output

# previous approach
# class Solution:
#     def missingNumber(self, nums: 'List[int]') -> int:
#         return (1+len(nums))*(len(nums))//2 - sum(nums)




# previous approach
# def missingNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     sum = 0
#     max = nums[0]
#     count = 0
#     for i in nums:
#         sum+=i
#         if i>max:
#             max = i
#     if max!=len(nums):
#         return len(nums)
#     else:
#         ought =  max * (len(nums) +1) /2
#         return int(ought-sum)
#
#
# print(missingNumber([0]))
# print(missingNumber([9,6,4,2,3,5,7,0,1]))