class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        if nums == []: return 0
        none_cnt = 0
        cnt = 1
        left = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == left:
                cnt += 1
                if cnt > 2:
                    nums[i] = None  # fill the repeated ones as None
                    none_cnt += 1
            else:
                left = nums[i]
                cnt = 1

        output = len(nums) - none_cnt
        i = 0
        while i < output:
            if nums[i] == None:  # swap with the first not None
                j = i + 1
                while j < len(nums):
                    if nums[j] != None:
                        nums[i] = nums[j]
                        nums[j] = None
                        break
                    j += 1
            i += 1

        return output



# previous approach
# def removeDuplicates( nums: 'List[int]'):
#     # 2 pointers
#     if len(nums) < 3:
#         return len(nums)
#     else:
#         l, r = 0, 2
#         while r < len(nums):
#             if nums[l] == nums[r]:
#                 nums.remove(nums[r])
#             else:
#                 r += 1
#                 l += 1
#
#     return len(nums)


# original code
#         if len(nums)<3:
#             return len(nums)
#         else:
#             r_cnt = 0
#             curr_cnt = 1
#             i = 1

#             while i < len(nums):
#                 if nums[i] == nums[i-1]:
#                     curr_cnt += 1
#                 else:
#                     curr_cnt = 1
#                 if curr_cnt > 2:
#                     r_cnt += 1
#                     nums.remove(nums[i])
#                     curr_cnt -= 1
#                 else:
#                     i+=1

#         return len(nums)

#
# nums = [1,1,1,2,2,3]
# len = removeDuplicates(nums)
# for i in range(len):
#     print(nums[i])
#
#
#
#
#
#



