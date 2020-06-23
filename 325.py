class Solution:
    def maxSubArrayLen(self, nums: 'List[int]', k: int) -> int:
        hmp = {}  # record curr rolling sum
        curr = 0
        output = 0
        for i, n in enumerate(nums):
            curr += n
            if curr not in hmp:
                hmp[curr] = []
            hmp[curr].append(i)

            if curr == k:
                output = max(output, i + 1)

            if curr - k in hmp:  # the diff was seen before
                output = max(output, i - hmp[curr - k][0])

        return output