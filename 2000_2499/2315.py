class Solution:
    def countAsterisks(self, s: str) -> int: #O(N | N)
        arr = s.split('|')
        cnt = 0  
        for i, a in enumerate(arr): #skip the odd sequence, as it's should not be included
            cnt += 0 if i%2 else a.count('*')
        return cnt
                
