class Solution:
    def maxPerformance(self, n: int, speed: 'List[int]', efficiency: 'List[int]', k: int) -> int:
        eng = sorted(list(zip(speed, efficiency)), reverse = True, key = lambda x: x[1])
        totalSpeed =0
        output = 0
        pq = []
        heapq.heapify(pq)
        for s , eff in eng:
            if len(pq) > k-1:
                totalSpeed -= heapq.heappop(pq) #lowest speed in the pq
            heapq.heappush(pq, s)
            totalSpeed += s
            output = max(output, totalSpeed * eff)
        return output % (10**9+7)


# previous approach
# class Solution:
#     def maxPerformance(self, n: int, speed: 'List[int]', efficiency: 'List[int]', k: int) -> int:
#         eng = sorted(list(zip(speed, efficiency)), reverse=True, key=lambda x: x[1])
#         output = 0
#         totalSpeed = 0
#         pq_speed = []
#         heapq.heapify(pq_speed)
#         for s, eff in eng:  # assuming current has the lowest eff
#             if len(pq_speed) > k - 1:
#                 totalSpeed -= heapq.heappop(pq_speed)
#             heapq.heappush(pq_speed, s)
#             totalSpeed += s
#             output = max(output, totalSpeed * eff)
#         return output % (10 ** 9 + 7)
#
#
