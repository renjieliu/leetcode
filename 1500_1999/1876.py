class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        else:
            hmp = {}
            for i in range(3):
                if s[i] not in hmp:
                    hmp[s[i]] = 0
                hmp[s[i]] += 1
            output = 1 if len(hmp) == 3 else 0
            for i in range(3, len(s)):
                if s[i] not in hmp:
                    hmp[s[i]] = 0
                hmp[s[i]] += 1
                hmp[s[i-3]] -= 1
                if hmp[s[i-3]] == 0 :
                    del hmp[s[i-3]]
                output += 1 if len(hmp) == 3 else 0
            return output
