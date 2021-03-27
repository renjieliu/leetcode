class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = len(s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                cnt += 1 if s[i:j+1] == s[i:j+1][::-1] else 0
        return cnt
