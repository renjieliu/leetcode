class Solution:
    def maximumGap(self, nums: 'List[int]') -> int:
        lo = min(nums)
        hi = max(nums)
        n = len(nums)  # distribute the number to the (hi-lo) bucket
        hmp = {}
        if lo == hi or n <= 2:
            return hi - lo
        for num in nums:
            bucket = (num - lo) * n // (hi - lo)  # distribute the number to the bucket
            if bucket not in hmp:
                hmp[bucket] = []
            hmp[bucket].append(num)
        output = 0
        arr = [[min(hmp[i]), max(hmp[i])] for i in range(n + 1) if i in hmp]
        for i in range(1, len(arr)):
            output = max(arr[i][0] - arr[i - 1][1], output)  # the result is the diff of currMin and prevMax
        return output
