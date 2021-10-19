class Solution:
    def countKDifference(self, nums: 'List[int]', k: int) -> int:
        hmp = {}
        for n in nums:
            if n not in hmp:
                hmp[n] = 0
            hmp[n] += 1
        cnt = 0
        for n, v in hmp.items():
            if n+k in hmp:
                cnt += v * hmp[n+k]
        return cnt


