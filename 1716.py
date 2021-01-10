class Solution:
    def totalMoney(self, n: int) -> int:
        rem_start = 1 + (n//7)
        rem_end = rem_start + (n%7) - 1
        rem_total = (rem_start+rem_end) * (rem_end - rem_start+1) //2
        prev_total =  n//7 *(28+ (28+(n//7-1)*7))//2 #sum of the weeks before the last week Sn=na1+n(n-1)d/2=n(a1+an)/2
        return prev_total+ rem_total