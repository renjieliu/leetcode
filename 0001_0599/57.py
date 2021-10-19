class Solution:
    def insert(self, intervals: 'List[List[int]]', newInterval: 'List[int]') -> 'List[List[int]]':
        def cover(A, B):
            return True if A[0] <= B[1] <= A[1] or B[0] <= A[1] <= B[1] else False

        intervals.append(newInterval)
        if intervals == [[]]:
            return [[]]
        else:
            intervals.sort()
            output = [intervals[0]]
            i = 1
            while i < len(intervals):
                if cover(output[-1], intervals[i]):
                    output[-1] = [min(output[-1][0], intervals[i][0]), max(output[-1][1], intervals[i][1])]
                else:
                    output.append(intervals[i])
                i += 1
            return output