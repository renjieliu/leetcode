class Solution:
    def arrayRankTransform(self, arr: 'List[int]') -> 'List[int]':
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = -1
        k = sorted(hmp.keys())
        i = 0
        while i < len(k):
            hmp[k[i]] = i+1
            i+=1
        output = []
        for a in arr:
            output.append(hmp[a])
        return output