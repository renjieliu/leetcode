class Solution:
    def kWeakestRows(self, mat: 'List[List[int]]', k: int) -> 'List[int]':
        hmp = {}
        for r in range(len(mat)):
            s = 0
            c = 0
            while c < len(mat[r]):
                if mat[r][c] == 1:
                    s += mat[r][c]
                else:
                    break
                c += 1
            if s not in hmp:
                hmp[s] = []
            hmp[s].append(r)
        output = []
        lst = sorted(hmp.keys())
        for i in lst:
            for r in hmp[i]:
                output.append(r)
        return output[:k]


