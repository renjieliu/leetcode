class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        hmp = {}
        i = 0
        while i < len(nums):
            if nums[i] not in hmp:
                hmp[nums[i]] = []
            hmp[nums[i]].append(i)
            i += 1
        for k in hmp.keys():
            if k * 2 == target:
                if len(hmp[k]) > 1:
                    return [hmp[k][0], hmp[k][1]]
            elif target - k in hmp:
                return [hmp[target - k][0], hmp[k][0]]

