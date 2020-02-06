class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c]+=1
        even = 0
        odd = 0
        for v in hmp.values():
            if v %2 ==0:
                even +=1
            else:
                odd +=1
        if odd > 1:
            return False
        else: # regardless of how many even are there... even 0.
            return True
