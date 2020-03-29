class Solution:
    def findLucky(self, arr: 'List[int]') -> int:
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a] += 1
        output = -float('inf')
        for k, v in hmp.items():
            if k == v:
                output = max(output, v)
        return -1 if output == -float('inf') else output

