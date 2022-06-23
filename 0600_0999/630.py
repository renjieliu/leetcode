class Solution:
    def scheduleCourse(self, courses: 'List[List[int]]') -> int: # O( nlogn | n)
        courses.sort(key = lambda x: x[1]) # sort by the deadline
        pq = []
        end = 0
        for duration, deadline in courses:
            end += duration
            heapq.heappush(pq, -duration) #add the duration to the min heap
            while end > deadline and pq: #take out the longest course previously taken.
                end += heapq.heappop(pq) # duration in the pq is negative already

        return len(pq)
    



# previous solution


# class Solution:
#     def scheduleCourse(self, courses: 'List[List[int]]') -> int:
#         courses.sort(key = lambda x: x[1])
#         currEnd = 0
#         arr = []
#         heapq.heapify(arr)
#         for duration, end in courses: #take the shortest duration, and end as early as possible
#             currEnd += duration
#             heapq.heappush(arr, -duration)
#             while currEnd > end and len(arr)>0:
#                 currEnd += heapq.heappop(arr)
#         return len(arr)

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