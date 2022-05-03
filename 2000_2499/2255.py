class Solution:
    def countPrefixes(self, words: 'List[str]', s: str) -> int: #O(N | 1)
        output = 0 
        for w in words:
            output += 1 if w == s[:len(w)] else 0 
        return output
    

