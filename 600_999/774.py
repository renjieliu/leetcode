class Solution(object):
    def minmaxGasDist(self, stations: 'List[int]', k: int) -> float:
        def possible(arr, v, k): #to check if possible to have current max distance = v
            cnt = 0
            for i in range(1, len(arr)):
                cnt += (arr[i] - arr[i-1]) // v # how many stations need to add in between
            # print(v, cnt)
            return cnt <= k


        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(stations, mi, k):
                hi = mi
            else:
                lo = mi
        return lo


# class Solution: #heap, TLE
#     def minmaxGasDist(self, stations: List[int], k: int) -> float:
#         pq = [] #(-part_length, original_length, num_parts)
#         for i in range(len(stations) - 1):
#             x, y = stations[i], stations[i+1]
#             pq.append((x-y, y-x, 1))
#         heapq.heapify(pq)

#         for _ in range(k):
#             negnext, orig, parts = heapq.heappop(pq)
#             parts += 1
#             heapq.heappush(pq, (-(orig / float(parts)), orig, parts))

#         return -pq[0][0]


