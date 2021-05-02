class Solution:
    def scheduleCourse(self, courses: 'List[List[int]]') -> int:
        heap, currFinish = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            currFinish += t
            heapq.heappush(heap, -t)
            while currFinish > end:
                saved = heapq.heappop(heap)
                currFinish += saved
        return len(heap)

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