class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1
        atleast = 0
        atmost = 0
        for i, v in hmp.items():
            if v % 2 != 0:  # if it's odd length, it need to be standalone.
                atleast += 1
            atmost += v
        # print(atleast, atmost, hmp)
        return True if atleast <= k <= atmost else False

