class Solution:
    def wiggleSort(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(arr, a, b):
            t = arr[a]
            arr[a] = arr[b]
            arr[b] = t

        nums.sort()
        half = len(nums) // 2 + (1 if len(
            nums) % 2 == 1 else 0)  # start from half way, each time, pick one from the first half and swap with the one from the second half.
        i = 0
        while i < len(nums):
            # print(nums)
            if i % 2 != 0:
                swap(nums, i, half)
                half += 1
            i += 1
