class Solution:
    def furthestBuilding(self, heights: 'List[int]', bricks: int, ladders: int) -> int:
        arr = []
        heapq.heapify(arr)
        for i in range(len(heights)-1): #keep using the ladder, if no ladder left, use bricks for the fist gaps
            gap = heights[i+1] - heights[i]
            if gap > 0:
                heapq.heappush(arr, gap)
                if len(arr) > ladders:
                    bricks -= heapq.heappop(arr)
                    if bricks < 0:
                        return i
        return len(heights) - 1
