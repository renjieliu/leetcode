class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            output = 0
            for i in range(32):
                currTotal = 0
                for n in nums:
                    currTotal += ((n >> i) & 1)  # add current bit
                currTotal %= 3  # it's either 1 or 0

                output = output | (currTotal << i)  # set the number for current bit

            return output - 2 ** 32 if output >= 2 ** 31 else output