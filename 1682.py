class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}

        def helper(s, l, r, left, dp):  # the left is the previous letter
            if (l, r, left) in dp:
                return dp[(l, r, left)]
            else:
                if l >= r:
                    dp[(l, r, left)] = 0
                else:
                    if s[l] == s[r] and s[l] != left:
                        return 2 + helper(s, l + 1, r - 1, s[l], dp)
                    else:
                        dp[(l, r, left)] = max(helper(s, l + 1, r, left, dp), helper(s, l, r - 1, left, dp))

                return dp[(l, r, left)]

        return helper(s, 0, len(s) - 1, '', dp)

