class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = len(s) 
        hmp = {}
        for c in s :
            if c not in hmp:
                hmp[c] = 0 
            hmp[c] += 1 
            if hmp[c] >= 2: 
                cnt += hmp[c]-1 # current c link with all the previous c
        return cnt 

    
