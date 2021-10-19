class Solution:
    def sortColors(self, nums: 'List[int]') -> None: # O(N)
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(arr, i, j):
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

        lastZero = None  # last zero place
        firstTwo = None  # first two place
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                if lastZero == None:
                    lastZero = 0
                else:
                    lastZero += 1
                swap(nums, i, lastZero)
                if lastZero == i:  # all zeros in front of current
                    i += 1
            elif nums[i] == 2:
                if firstTwo == None:
                    firstTwo = len(nums) - 1
                    swap(nums, i, firstTwo)
                elif firstTwo > i:  # all two after here
                    firstTwo -= 1
                    swap(nums, i, firstTwo)
                else:
                    i += 1
            else:
                i += 1

            # print(nums)

# old approach - O(n2)
# def sortColors(nums: 'List[int]'):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     i = 0
#     length = len(nums)
#     cnt = 0
#     while i < length:
#         #print(nums )
#         cnt += 1
#         if nums[i] == 0:
#             del nums[i]
#             nums.insert(0, 0)
#             i+=1
#         elif nums[i] == 2:
#             del nums[i]
#             nums.append(2)
#         else:
#             i += 1
#
#         if cnt == length:
#             break
#
#     return nums
#
#
# print(sortColors([2, 0, 2, 1, 1, 0]))
