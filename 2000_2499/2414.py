class Solution:
    def longestContinuousSubstring(self, s: str) -> int: # O( N | 1 )
        r = 1
        output = 1
        local = 1
        while r < len(s): # go through s, and compare with the previous character
            if ord(s[r]) == ord(s[r-1]) + 1:
                local += 1
            else:
                local = 1
            output = max(output, local)
            r += 1 
        
        return output

