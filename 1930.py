class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hmp = {}
        for i, c in enumerate(s):
            if c not in hmp:
                hmp[c] = []
            hmp[c].append(i) #record the index of each character appearance
        cnt = 0
        for k, v in hmp.items():
            if len(v)>=2:
                start = v[0]+1
                end = v[-1]
                in_between = set(s[start:end]) #find distinct character in between start index and end index
                cnt += len(in_between)
        return cnt


