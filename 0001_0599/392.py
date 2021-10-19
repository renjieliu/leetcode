class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for c in s:
            if c in t[ptr:]:
                ptr += t[ptr:].index(c)+1
            else:
                return False
        return True