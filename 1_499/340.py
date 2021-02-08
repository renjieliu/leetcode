class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = r = 0
        hmp = {}
        output = 0
        while r < len(s):
            c = s[r]
            if c not in hmp:
                hmp[c] = 0
            hmp[c] +=1
            while l<=r and len(hmp) > k: #move the left pointer, until the distinct count is <= k
                hmp[s[l]]-=1
                if hmp[s[l]] ==0:
                    del hmp[s[l]]
                l+=1
            output = max(r-l+1, output)
            r+=1
        return output