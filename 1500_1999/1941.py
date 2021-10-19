class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        arr = [0] * 26
        baseline = 0
        for c in s:
            pos = ord(c) - ord('a')
            arr[pos] += 1
            baseline = max(baseline, arr[pos])
        for a in arr:
            if a != 0 and a != baseline:
                return False
        return True

        # hmp = {}
        # for c in s:
        #     if c not in hmp:
        #         hmp[c]  = 0
        #     hmp[c] +=1
        # return len(set(hmp.values())) == 1

