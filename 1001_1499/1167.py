class Solution:
    def connectSticks(self, sticks: 'List[int]') -> int:
        heapq.heapify(sticks) #using a heap to pop smallest 2 items each time, and add the sum back to the heap
        cost = 0
        while len(sticks) > 1 :
            curr = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += curr
            heapq.heappush(sticks, curr)
        return cost

