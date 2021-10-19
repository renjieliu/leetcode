class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def sameHash(h1, h2):
            if len(h1) != len(h2):
                return False
            for k, v in h1.items():
                if k not in h2 or h2[k] != v:
                    return False
            return True

        if s1 == "":
            return True if s2 != "" else False
        lkp = {}
        for c in s1:
            if c not in lkp:
                lkp[c] = 0
            lkp[c] += 1
        left = 0
        curr = {}
        for right in range(len(s2)):
            if s2[right] not in curr:
                curr[s2[right]] = 0
            curr[s2[right]] += 1

            if right - left + 1 == len(s1):
                if sameHash(lkp, curr):
                    return True
                else:
                    curr[s2[left]] -= 1
                    if curr[s2[left]] == 0:
                        del curr[s2[left]]
                    left += 1

        return False