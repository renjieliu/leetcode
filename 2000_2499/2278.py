class Solution:
    def percentageLetter(self, s: str, letter: str) -> int: #O(N | 1)
        return s.count(letter) * 100 // len(s)
    
