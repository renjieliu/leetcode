class Solution:
    def maxPower(self, s: str) -> int:
        currStart = 0
        output = 1
        i = 1
        while i < len(s):
            if s[i] != s[i-1]:
                output = max(output, i-currStart)
                currStart = i
            i+=1
        output = max(output, i-currStart)
        return output