class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hmp  ={}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c]+=1
        odd = 0
        for k, v in hmp.items():
            odd+= v%2
        return odd <=1