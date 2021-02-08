class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmp = {}
        for i,c in enumerate(s):
            if c not in hmp:
                hmp[c] = []
            hmp[c].append(i)
        output = []
        for v in hmp.values():
            if len(v) ==1:
                output += v
        output.sort()
        return -1 if len(output) ==0 else output[0]