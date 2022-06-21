class Solution:
    def furthestBuilding(self, heights: 'List[int]', bricks: int, ladders: int) -> int: #(NlogN | N)
        pq = []
        for i in range(1, len(heights)):
            delta = heights[i] - heights[i-1] 
            if delta > 0:
                heapq.heappush(pq, delta) #min heap, to use bricks for the smallest gaps
                if len(pq) > ladders: # it cannot be covered by ladders
                    bricks -= heapq.heappop(pq)
                    if bricks < 0: #not enough bricks, it means current loc cannot be reached
                        return i-1
            
        return len(heights)-1 # it reaches the end of the buildings

    


# previous solution

# class Solution:
#     def furthestBuilding(self, heights: 'List[int]', bricks: int, ladders: int) -> int:
#         arr = []
#         heapq.heapify(arr)
#         for i in range(len(heights)-1): # use ladder first, if runs out of letter, use bricks for min(height) in the heap
#             delta = heights[i] - heights[i+1]
#             if delta < 0:
#                 heapq.heappush(arr, abs(delta))
#                 if len(arr) > ladders:
#                     bricks -= heapq.heappop(arr)
#                     if bricks < 0:
#                         return i
#         return len(heights)-1

# previous approach
# class Solution:
#     def furthestBuilding(self, heights: 'List[int]', bricks: int, ladders: int) -> int:
#         arr = []
#         heapq.heapify(arr)
#         for i in range(len(heights)-1): #keep using the ladder, if no ladder left, use bricks for the fist gaps
#             gap = heights[i+1] - heights[i]
#             if gap > 0:
#                 heapq.heappush(arr, gap)
#                 if len(arr) > ladders:
#                     bricks -= heapq.heappop(arr)
#                     if bricks < 0:
#                         return i
#         return len(heights) - 1
