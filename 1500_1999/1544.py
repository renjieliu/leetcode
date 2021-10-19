class Solution:
    def makeGood(self, s: str) -> str:
        def isGood(s):
            if len(s) <= 1:
                return [1]
            else:
                for i in range(1, len(s)):
                    if s[i].lower() == s[i - 1].lower() and s[i] != s[i - 1]:
                        return [0, i]
                return [1]

        res = isGood(s)
        while res[0] == 0:
            s = s[:res[1] - 1] + s[res[1] + 1:]
            res = isGood(s)
        return s


