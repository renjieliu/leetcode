class Solution:
    def kthSmallestSubarraySum(self, nums: 'List[int]', k: int) -> int:
        def helper(nums, v): # check how many subarray with sum < v
            cnt = 0
            l = r = 0
            total = 0
            while r < len(nums):
                total += nums[r]
                while total >= v and l<=r:
                    total -= nums[l]
                    l+=1
                cnt += r-l+1
                r+=1
            return cnt

        s = 0
        e = sum(nums)
        output = None
        while s<=e:
            mid = (s+e) // 2
            arrCount = helper(nums, mid)
            if arrCount < k: # number of arr with sum less than mid
                output = mid
                s = mid+1 # move the mid to larger
            else:
                e = mid -1 # mid is too big

        return output

