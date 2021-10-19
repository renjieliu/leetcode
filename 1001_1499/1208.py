class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l, r, curr, output = 0, 0, 0, 0
        while r < len(s):
            curr += abs(ord(s[r]) - ord(t[r]))
            if curr <= maxCost:
                output = max(r - l + 1, output)
            else:
                while l <= r:
                    curr -= abs(ord(s[l]) - ord(t[l]))
                    l += 1
                    if curr <= maxCost:
                        break
            r += 1
        return output

