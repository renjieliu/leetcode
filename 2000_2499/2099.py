class Solution:
    def maxSubsequence(self, nums: 'List[int]', k: int) -> 'List[int]':
        hmp = {}
        for i, n in enumerate(nums):
            if n not in hmp:
                hmp[n] = []
            hmp[n].append(i)
        
        locs = []
        for n in sorted(nums)[-k:]: #find the location of each number
            locs.append(hmp[n].pop(0))
        
        locs.sort() #sort the location to make it a subsequence of the original array
        output = []
        for loc in locs:
            output.append(nums[loc])    
        return output

    
    
