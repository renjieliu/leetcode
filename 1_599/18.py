class Solution:
    def fourSum(self, nums: 'List[int]', target: int) -> 'List[List[int]]':
        nums.sort() #O(N3), fixed first 3, find 4th, and check if first 3 is seen to speed up.
        seen = set()
        hmp = {}
        for i , n in enumerate(nums):
            hmp[n] = [i]

        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i], nums[j], nums[k]) not in seen:
                        rem = target-sum((nums[i], nums[j], nums[k]))
                        if rem in hmp and hmp[rem][0] > k:
                            output.append([nums[i], nums[j], nums[k],nums[hmp[rem][0]]])
                            seen.add((nums[i], nums[j], nums[k]))
        return output
                            
