class Solution:
    def countPoints(self, rings: str) -> int:
        hmp = {}
        cnt = 0
        for i, pos in enumerate(rings):
            if i % 2:
                color = rings[i-1]
                if pos not in hmp:
                    hmp[pos] = set()
                hmp[pos].add(color)
        for k, v in hmp.items():
            cnt += 1 if len(v) == 3 else 0
        return cnt
    
