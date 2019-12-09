class Solution:
    def smallestDivisor(self, nums: 'List[int]', threshold: int) -> int:
        def f(arr, d):
            output = 0
            for a in arr:
                output += a//d + (1 if a%d!=0 else 0)
            return output
        s = 1
        e = max(nums)
        output = float('inf')
        while s<=e: #binary search to find the target number
            mid = (s+e)//2
            t = f(nums,mid)
            if t==threshold:
                output= min(output,mid)
                e = mid -1
            elif t > threshold: #curr mid should be shifted to the right
                s=mid+1
            elif t<= threshold:
                e=mid-1
            
        if output ==float('inf'):
            return s
        else:
            return output
        
