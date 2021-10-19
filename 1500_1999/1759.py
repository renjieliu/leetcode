class Solution:
    def countHomogenous(self, s: str) -> int:
        if len(s) == 1: return 1
        mod = 10**9+7
        left = right = 0
        output = 0
        while right < len(s):
            if s[right] != s[left]:
                length = right-1 - left +1 #previous homogeneous string
                output += (1 + length)* length//2
            while s[left] != s[right]:
                left += 1
            right += 1

        right = len(s)-1
        length = right - left +1 #last homogeneous string
        output += (1 + length)* length//2


        return output % mod

