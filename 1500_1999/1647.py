class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s) == 1:  return 0
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1
        lkp = {}
        for k, v in hmp.items():
            if v not in lkp:
                lkp[v] = []
            lkp[v].append(k)
        # print(lkp)
        lst = list(lkp.keys())
        output = 0
        for l in lst:
            if len(lkp[l]) > 1:
                for c in lkp[l][1:]:
                    find = 0
                    for i in range(l, -1, -1):
                        if i not in lkp:
                            lkp[i] = None
                            find = i
                            break
                    output += (l - find)

        return output
