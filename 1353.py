class Solution:
    def maxEvents(self, events: 'List[List[int]]') -> int:
        events.sort(key = lambda x: x[1])
        cnt = 0
        days = {}
        for a, b in events:
            for i in range(a, b+1):
                if i not in days:
                    days[i] = 1
                    break
        return len(days)