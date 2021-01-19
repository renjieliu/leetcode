class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        output = ""
        for i in range(len(s)) :
            for j in range(len(s), i, -1):
                curr = s[i:j]
                if len(curr) <= len(output):
                    break
                elif curr == curr[::-1]:
                    if len(curr) > len(output):
                        output = curr
        return output
