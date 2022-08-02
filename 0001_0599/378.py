class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: int) -> int: #O( NlogN | N )
        pq = []
        for i, r in enumerate(matrix):
            heapq.heappush(pq, (r[0], i, 0)) #output, row, col
        while k:
            output, r, c = heapq.heappop(pq)
            if c+1 < len(matrix[0]):
                heapq.heappush(pq, (matrix[r][c+1], r, c+1)) # add the next element on the same row to the heap
            k-=1
        return output





# previous solution

# class Solution:
#     def kthSmallest(self, matrix: 'List[List[int]]', k: int) -> int:
#         pq = []
#         heapq.heapify(pq)
#         for r in matrix:
#             for c in r:
#                 heapq.heappush(pq, c)
#         cnt = 0
#         while cnt < k-1:
#             heapq.heappop(pq)
#             cnt += 1
#         return heapq.heappop(pq)


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
