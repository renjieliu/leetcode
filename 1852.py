class Solution:
    def distinctNumbers(self, nums: 'List[int]', k: int) -> 'List[int]':
        hmp = {}
        ans = []
        for n in nums[:k]:
            if n not in hmp:
                hmp[n] = 0
            hmp[n]+=1
        ans.append(len(hmp)) # initialize the ans
        l = 0
        r = k
        while r < len(nums): #add right item to the hmp, remove the left previous item, advance both pointer
            if nums[r] not in hmp:
                hmp[nums[r]]  = 0
            hmp[nums[r]] += 1
            hmp[nums[l]] -= 1
            if hmp[nums[l]] == 0:
                del hmp[nums[l]]
            ans.append(len(hmp))
            l+=1
            r+=1
        return ans