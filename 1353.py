class Solution:
    def maxEvents(self, events: 'List[List[int]]') -> int:
        events.sort()
        currDate = 0
        live = []  # heapq
        output = 0
        i = 0
        while live or i < len(events):
            if live == []:
                currDate = events[i][0]
            while live and live[0] < currDate:  # take out the ones already expired
                heapq.heappop(live)
            while i < len(events) and events[i][0] == currDate:
                print(i, live, currDate)
                heapq.heappush(live, events[i][1])  # need to sort the end date
                i += 1
            if live:
                heapq.heappop(live)
                output += 1
                currDate += 1
        return output


    # class Solution:
#     def maxEvents(self, events: 'List[List[int]]') -> int:
#         events.sort(key = lambda x: x[1])
#         cnt = 0
#         days = {}
#         for a, b in events:
#             for i in range(a, b+1):
#                 if i not in days:
#                     days[i] = 1
#                     break
#         return len(days)