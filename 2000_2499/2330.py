class Solution:
    def makePalindrome(self, s: str) -> bool: #O( N | 1 )
        cnt = 0 
        for i in range(len(s)//2): # no need to the mid letter for odd-length s
            cnt += (s[i] != s[-i-1]) #to check if current pair is same. if not the same: cnt+1
        return cnt <= 2

