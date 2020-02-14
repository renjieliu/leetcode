"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        def merge(A, B):  # to merge the A and B intervals
            output = []
            for a in A:
                for b in B:
                    if (b[0] <= a[1] <= b[1] or a[0] <= b[1] <= a[1]):
                        output.append([max(a[0], b[0]), min(a[1], b[1])])
            return output

        i = 0
        free = []
        while i < len(schedule):  # find free time for each one
            free.append([])
            s = 0
            while s < len(schedule[i]):
                if s == 0:
                    free[-1].append([-float('inf'), schedule[i][s].start])
                else:
                    free[-1].append([schedule[i][s - 1].end, schedule[i][s].start])
                s += 1
            free[-1].append([schedule[i][-1].end, float('inf')])
            i += 1
        # print(free)
        avail = free[0]
        i = 1
        while i < len(free):  # keep merging free time
            avail = merge(avail, free[i])
            i += 1
        output = []
        for a in avail:
            if a[0] != -float('inf') and a[1] != float('inf') and a[0] != a[1]:
                o = Interval()
                o.start = a[0]
                o.end = a[1]
                output.append(o)
        return output

