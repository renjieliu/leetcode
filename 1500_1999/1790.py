class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        for i, c in enumerate(s1):
            diff += 1 if c != s2[i] else 0
        return diff <= 2 and set(s1) == set(s2)