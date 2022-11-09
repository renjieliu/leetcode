class Solution:
    def maximumSubarraySum(self, nums: 'List[int]', k: int) -> int: # O( N | N )
        hmp = defaultdict(lambda: [-float('inf')]) #set the default last loc as -float('inf')
        output = 0
        l = r = 0
        curr = 0
        while r < len(nums):
            n = nums[r]
            curr += n
            if r - hmp[n][-1] + 1 <= k: # the last seen location is too close
                while l <= hmp[n][-1]:
                    curr -= nums[l]
                    l += 1
            
            while l <= r and r - l + 1 > k:  # move the left pointer until the window length is k
                curr -= nums[l]
                l += 1

            if r - l + 1 == k:
                output = max(output, curr)
            # print(l, r, curr, output)
            hmp[n].append(r)
            r += 1
        
        
        return output 
            
            

