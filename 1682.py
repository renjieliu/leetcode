class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        hmp = {}

        def dp(l, r, prev):
            if (l, r, prev) in hmp:
                return hmp[(l, r, prev)]
            else:
                if l >= r: return 0
                if s[l] == s[r] and (s[l] != prev):
                    return 2 + dp(l + 1, r - 1, s[l])
                else:  # it's not the same, so either move the right pointer to the left, or the left pointer to the right
                    hmp[(l, r, prev)] = max(dp(l + 1, r, prev), dp(l, r - 1, prev))
                    return hmp[(l, r, prev)]

        return dp(0, len(s) - 1, '')
