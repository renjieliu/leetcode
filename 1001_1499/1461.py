class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        lkp = set()
        for i in range(len(s)+1-k):
            lkp.add(s[i:i+k])
        return len(lkp) == 2**k