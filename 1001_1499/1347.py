class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hmp_s = {}
        for c in s:
            if c not in hmp_s:
                hmp_s[c] = 0
            hmp_s[c]+=1
        hmp_t = {}
        for c in t:
            if c not in hmp_t:
                hmp_t[c] =0
            hmp_t[c] +=1
        output = 0

        for k in hmp_s.keys():
            if k in hmp_t:
                hmp_s[k] -= hmp_t[k]
            if hmp_s[k]>0: #check in hmp_s, how many need to be replaced.
                output+=hmp_s[k]
        return output