class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int: # O( 365 | 1 )
        cnt = 0 
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(1, 13): # go through each month, and see if it's between the 2 days and overlapped for 2 person. To avoid month/day calculation.
            M = ("0" if m < 10 else "") + str(m)
            for d in range(1, days[m-1]+1): # number of days from days arr
                D = ("0" if d < 10 else "") + str(d)
                cnt += (arriveAlice <= M + "-" + D <= leaveAlice and arriveBob <= M + "-" + D <= leaveBob)
        return cnt


