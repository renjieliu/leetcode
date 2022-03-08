class Solution:
    def mostFrequent(self, nums: 'List[int]', key: int) -> int:
        hmp = defaultdict(lambda:0)
        output = mx = 0
        for i in range(1, len(nums)):
            if nums[i-1] == key: # if prev is key, add current 1 more time
                hmp[nums[i]] += 1
                if hmp[nums[i]] >= mx:
                    mx = hmp[nums[i]]
                    output = nums[i]
        return output

    
