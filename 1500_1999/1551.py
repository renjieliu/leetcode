class Solution:
    def minOperations(self, n: int) -> int:
        target = (1 + (n//2)*2 ) if n % 2 == 1 else ((1 + (n//2) * 2) + (1 + (n//2-1) * 2))//2 #to find the middle number
        cnt = n//2
        return (2*cnt + cnt*(cnt-1)) if target % 2 == 1 else (cnt + (cnt*(cnt-1))) #it's 1.3.5... cnt or 2.4.6..cnt