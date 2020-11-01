class Solution:
    def canAttendMeetings(self, intervals:'List[List[int]]') -> bool:
        if len(intervals) == 0 :
            return True
        intervals.sort(key=lambda x:x[0])
        currE = intervals[0][1]
        for s, e in intervals[1:]:
            if s < currE:
                return False
            currE = e
        return True