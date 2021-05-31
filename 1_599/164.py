class Solution:
    def maximumGap(self, nums: 'List[int]') -> int:  # using bucket sort, max is the currMin-prevMax
        hi = max(nums)
        lo = min(nums)
        total = len(nums)
        hmp = {}
        if hi == lo:  # or total <= 2:
            return 0
        for n in nums:
            n_tile = (n - lo) * total // (hi - lo)
            if n_tile not in hmp:
                hmp[n_tile] = []
            hmp[n_tile].append(n)
        arr = []
        for i in range(total + 1):
            if i in hmp:
                arr.append([min(hmp[i]), max(hmp[i])])

        output = arr[0][1] - arr[0][0]  # the initial value
        for i in range(1, len(arr)):
            output = max(output, arr[i][0] - arr[i - 1][1])
        return output


# previous approach
# class Solution:
#     def maximumGap(self, nums: 'List[int]') -> int:
#         lo = min(nums)
#         hi = max(nums)
#         n = len(nums)  # distribute the number to the (hi-lo) bucket
#         hmp = {}
#         if lo == hi or n <= 2:
#             return hi - lo
#         for num in nums:
#             bucket = (num - lo) * n // (hi - lo)  # distribute the number to the bucket
#             if bucket not in hmp:
#                 hmp[bucket] = []
#             hmp[bucket].append(num)
#         output = 0
#         arr = [[min(hmp[i]), max(hmp[i])] for i in range(n + 1) if i in hmp]
#         for i in range(1, len(arr)):
#             output = max(arr[i][0] - arr[i - 1][1], output)  # the result is the diff of currMin and prevMax
#         return output
