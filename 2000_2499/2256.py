class Solution:
    def minimumAverageDifference(self, nums: 'List[int]') -> int:
        prefix = [nums[0]] # prefix sum
        for n in nums[1:]:
            prefix.append(prefix[-1] + n)
        total = prefix[-1] 
        
        minn = float('inf')
        output = None
        div = lambda A, B: 0 if B == 0 else A // B #per question, the average of 0 elements is 0
        for i in range(len(nums)):
            A = prefix[i] // (i+1)
            B = div(total - prefix[i], (len(nums) - (i+1)))
            diff = abs(A-B) 
            if diff < minn:
                minn = diff 
                output = i
        return output
    
    
