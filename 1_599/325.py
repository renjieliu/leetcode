class Solution:
    def maxSubArrayLen(self, nums: 'List[int]', k: int) -> int:
        hmp = {0:-1} # currSum: location, initialize to -1
        output = 0
        curr = 0 #accumulate sum

        for i, n in enumerate(nums):
            curr += n
            if curr-k in hmp: #it means currRangeSum is k
                output = max(output, i-hmp[curr-k])

            if curr not in hmp: # if curr in hmp, no need to add. we check the first location, to maximize output
                hmp[curr] = i
        return output



# previous approach
# class Solution:
#     def maxSubArrayLen(self, nums: 'List[int]', k: int) -> int:
#         hmp = {}  # record curr rolling sum
#         curr = 0
#         output = 0
#         for i, n in enumerate(nums):
#             curr += n
#             if curr not in hmp:
#                 hmp[curr] = []
#             hmp[curr].append(i)
#
#             if curr == k:
#                 output = max(output, i + 1)
#
#             if curr - k in hmp:  # the diff has seen before
#                 output = max(output, i - hmp[curr - k][0])
#
#         return output
#
