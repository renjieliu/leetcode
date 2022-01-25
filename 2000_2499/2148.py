class Solution:
    def countElements(self, nums: 'List[int]') -> int:
        mi, mx = min(nums), max(nums)
        cnt = 0 
        for n in nums:
            if n != mi and n!=mx: #if it's not the minimum or maximum, then added it
                cnt += 1
        return cnt
    
