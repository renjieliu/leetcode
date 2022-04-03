class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        t = start^goal #to check how many 1's are in the xor'ed
        cnt = 0
        while t > 0:
            cnt += t%2
            t>>= 1
        return cnt 
    
