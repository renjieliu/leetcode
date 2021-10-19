class Solution:
    def findTheLongestSubstring(self, s: str) -> int: # use bitmap to store the repeating pattern
        ref = {'a': 1, 'e':2, 'i': 4, 'o':8 , 'u':16}
        output = 0
        curr = 0
        hmp = {0:-1}
        for i, c in enumerate(s): #to generate the pattern. If the pattern is same, then there's even number of aeiou in between
            if c in ref:
                curr = curr^ref[c]
            if curr not in hmp:
                hmp[curr]  = i
            else:
                output = max(output, i - hmp[curr])
        return output