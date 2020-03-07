class Solution:
    def sortString(self, s: str) -> str:
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1
        asc = sorted(list(hmp.keys()))
        desc = sorted(list(hmp.keys()), reverse=True)
        output = ""
        while hmp:
            i = 0
            while i < len(asc):
                a = asc[i]
                output += a
                hmp[a] -= 1
                if hmp[a] == 0:
                    del hmp[a]
                    asc.remove(a)
                    desc.remove(a)
                else:
                    i += 1
            i = 0
            while i < len(desc):
                d = desc[i]
                output += d
                hmp[d] -= 1
                if hmp[d] == 0:
                    del hmp[d]
                    desc.remove(d)
                    asc.remove(d)
                else:
                    i += 1

        return output



