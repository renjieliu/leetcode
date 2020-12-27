class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = b = 0
        for i in range(len(s)):
            a += 1 if s[i].lower() in ('a','e','i','o','u') and i < len(s)//2 else 0
            b += 1 if s[i].lower() in ('a','e','i','o','u') and i >= len(s)//2 else 0
        return a==b