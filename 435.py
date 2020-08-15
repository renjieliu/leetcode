class Solution:
    def eraseOverlapIntervals(self, intervals: 'List[List[int]]') -> int:
        if intervals ==  []: return 0
        intervals.sort(key = lambda x: x[1])
        cnt = 1
        curr = intervals[0]
        for s, e in intervals:
            if curr[1] <= s: #curr no overlapping
                cnt += 1
                curr = [s,e] #check the max can be grouped together
        return len(intervals)-cnt