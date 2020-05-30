class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hmp =  {}
        for i in range(len(s)+1-k):
            if s[i:i+k] not in hmp:
                hmp[s[i:i+k]] = None
        return False if len(hmp) < 2**k else True