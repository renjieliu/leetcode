class Solution:
    def maximumPopulation(self, logs: 'List[List[int]]') -> int:
        hmp = {}
        for a, b in logs:
            for i in range(a,b):
                if i not in hmp:
                    hmp[i] = 0
                hmp[i]+=1
        v = max(hmp.values())
        for k in sorted(list(hmp.keys())):
            if hmp[k] == v:
                return k

