class Solution:
    def maximumUniqueSubarray(self, nums: 'List[int]') -> int:
        l = r = 0
        output = -float('inf')
        lkp = set()
        window = 0
        while r < len(nums) :
            curr = nums[r]
            if curr not in lkp:
                lkp.add(curr)
                window+=curr
                output = max(output, window)
            else:
                while nums[l] != curr:
                    lkp.remove(nums[l])
                    window -= nums[l]
                    l+=1
                l+=1 #move it one more time to the start of curr window
                lkp.add(curr)
                output=max(output, window)
            r+=1
        return output