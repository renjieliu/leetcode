class Solution:
    def scheduleCourse(self, courses: 'List[List[int]]') -> int:
        courses.sort(key = lambda x: x[1])
        currEnd = 0
        arr = []
        heapq.heapify(arr)
        for duration, end in courses: #take the shortest duration, and end as early as possible
            currEnd += duration
            heapq.heappush(arr, -duration)
            while currEnd > end and len(arr)>0:
                currEnd += heapq.heappop(arr)
        return len(arr)

# previous approach
# class Solution:
#     def scheduleCourse(self, courses: 'List[List[int]]') -> int:
#         heap, currFinish = [], 0
#         for t, end in sorted(courses, key=lambda x: x[1]):
#             currFinish += t
#             heapq.heappush(heap, -t)
#             while currFinish > end:
#                 saved = heapq.heappop(heap)
#                 currFinish += saved
#         return len(heap)

# previous approach
# class Solution:
#     def scheduleCourse(self, courses: 'List[List[int]]') -> int:
#         heap, time = [], 0
#         for t, end in sorted(courses, key=lambda x: x[1]):
#             time += t
#             heapq.heappush(heap, -t)
#             if time > end:
#                 nt = heapq.heappop(heap)
#                 time += nt
#         return len(heap)