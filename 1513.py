class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9+7
        output = 0
        curr = 0
        for c in s:
            if c == "1":
                curr += 1
                output+=curr
            else:
                curr = 0
        return output%mod