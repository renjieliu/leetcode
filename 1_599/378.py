class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: int) -> int:
        pq = []
        heapq.heapify(pq)
        for r in matrix:
            for c in r:
                heapq.heappush(pq, c)
        cnt = 0
        while cnt < k-1:
            heapq.heappop(pq)
            cnt += 1
        return heapq.heappop(pq)


# previous approach
# def kthSmallest(matrix: 'List[List[int]]', k: int):
#     arr = []
#     for i in matrix:
#         arr += i
#
#     arr.sort()
#     return arr[k-1]
#
# print(kthSmallest( [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ], 8))
