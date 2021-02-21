class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(s):
            lower = set()
            upper = set()
            for c in s:
                if 97 <= ord(c) <= 122:
                    lower.add(ord(c) - 32)
                else:
                    upper.add(ord(c))
            return lower - upper == set() and upper - lower == set()

        output = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if isNice(s[i:j + 1]) and len(s[i:j + 1]) > len(output):
                    output = s[i:j + 1]
        return output