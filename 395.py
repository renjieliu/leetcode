class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s): return 0  # not possible for each character to repeat k times
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1

        for key, occur in hmp.items():
            if occur < k:  # if current character occurs less than k
                arr = s.split(key)  # using split to take the character out, and check the rest of the string
                return max([self.longestSubstring(a, k) for a in arr])

        return len(s)