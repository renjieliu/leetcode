class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hmp = {}
        output = -1
        for i in range(len(s)):
            if s[i] not in hmp:
                hmp[s[i]] = i
            else:
                output = max(output, i-hmp[s[i]]-1)
        return output