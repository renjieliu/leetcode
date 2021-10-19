class Solution:
    def maxSubarraySumCircular(self, A: 'List[int]') -> int:
        total = sum(A)
        minn = float('inf')
        curr_minn = 0
        for a in A:  # get the min range
            if curr_minn + a < a:
                curr_minn += a
            else:
                curr_minn = a
            minn = min(curr_minn, minn)

        maxx = -float('inf')  # get the maxx range
        curr_maxx = 0
        for a in A:
            if curr_maxx + a > a:
                curr_maxx += a
            else:
                curr_maxx = a
            maxx = max(curr_maxx, maxx)
        return max(maxx, total - minn) if maxx >= 0 else maxx