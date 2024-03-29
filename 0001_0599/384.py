import random

class Solution:

    def __init__(self, nums: 'List[int]'):
        self.ini = nums.copy()
        self.arr = nums

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.ini[::]
        return self.arr

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        output = []
        for a in self.arr:  # insert current number to a random location each time
            output.insert(random.randint(0, len(output)), a)
        return output

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()



# previous approach
# import random
#
#
# class Solution:
#
#     def __init__(self, nums: 'List[int]'):
#         self.nums = nums
#
#     def reset(self) -> 'List[int]':
#         """
#         Resets the array to its original configuration and return it.
#         """
#         return self.nums
#
#     def shuffle(self) -> 'List[int]':
#         """
#         Returns a random shuffling of the array.
#         """
#         new = []
#
#         arr = self.nums.copy()
#
#         i = len(arr) - 1
#
#         while i > 0:
#             end = len(arr) - 1
#             index = random.randint(0, end)
#             new.append(arr[index])
#             if index == i:
#                 arr = arr[:index]
#             else:
#                 arr = arr[:index] + arr[index + 1:]
#             i -= 1
#
#         return new + arr
#
# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.reset()
# # param_2 = obj.shuffle()