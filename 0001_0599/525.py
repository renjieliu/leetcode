class Solution:
    def findMaxLength(self, nums: 'List[int]') -> int:
        # treat 0 as -1 , 1 as 1,  if the sum is 0, then number equaled.
        # use the counter to trace the current sum, if the sum has been seen before, the number has been seen before,
        # the numbers b/w them satisfy the requirement
        # initialize the map, for the first item.
        # If the first item is 0 (-1), then it has not been seen, counter = -2, add to the hmp
        # if the first item is 1, then the counter is 0, which has not been seen before, counter = 1, add to the hmp

        hmp = {0: 0}
        # check the counter, if the counter number has been met before, meaning the sum between these 2 index is 0
        counter = 0
        output = 0
        for i in range(len(nums)):
            counter += (-1 if nums[i] == 0 else 1)
            if counter in hmp:  # the number has been seen before, check the diff between them
                output = max(output, i - hmp[counter] + 1)
            else:
                hmp[counter] = i + 1

        return output
