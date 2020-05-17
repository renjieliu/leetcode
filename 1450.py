class Solution:
    def busyStudent(self, startTime: 'List[int]', endTime: 'List[int]', queryTime: int) -> int:
        return sum(map( lambda x, queryTime: 1 if x[0]<=queryTime <=x[1] else 0, zip(startTime, endTime), [queryTime]*len(startTime)))