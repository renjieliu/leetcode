class Solution:
    def eraseOverlapIntervals(self, intervals: 'List[List[int]]') -> int:
        if intervals == [] :return 0
        arr = []
        intervals.sort(key = lambda x: x[1])
        #print(intervals)
        arr.append([intervals[0]])
        for s, e in intervals[1:]:
            placed = 0
            for a in arr:
                if s >= a[-1][1]:
                    a.append([s,e]) #no overlap here
                    placed = 1
                    break
            if placed == 0:
                arr.append([[s,e]])
        #print(arr)
        return len(intervals) - max( map( lambda x:len(x), arr) ) #the most can be grouped together
