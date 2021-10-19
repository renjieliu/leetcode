class Solution:
    def minMeetingRooms(self, intervals: 'List[List[int]]') -> int:
        if intervals == []: return 0
        intervals.sort()
        heap = [intervals[0][1]]
        firstEnd = intervals[0][1]
        output = 1
        for start, end in intervals[1:]:
            if start >= firstEnd:  # can use curr room
                heapq.heappop(heap)  # take out the curr room from the heap
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
            output = max(len(heap), output)
            firstEnd = heap[0]
        return output
