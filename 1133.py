class Solution:
    def largestUniqueNumber(self, A: 'List[int]') -> int:
        hmp = {}
        output = [-1]  # default return value
        for a in A:
            if a not in hmp:
                hmp[a] = 0
            hmp[a] += 1
        for k, v in hmp.items():
            if v == 1:
                output.append(k)
        return max(output)
