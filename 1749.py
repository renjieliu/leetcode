class Solution:
    def maxAbsoluteSum(self, nums: 'List[int]') -> int:
        output = max_so_far = max_ending_here = min_ending_here = min_so_far = 0
        for n in nums:
            max_ending_here = max(n, n+max_ending_here)
            max_so_far = max(max_so_far, max_ending_here)

            min_ending_here = min(n, n+min_ending_here)
            min_so_far = min(max_so_far, min_ending_here)
            output = max(output, max_so_far, abs(min_so_far))

        return output
