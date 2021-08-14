class Solution:
    def minStoneSum(self, piles: 'List[int]', k: int) -> int:
        pq = []
        total = sum(piles)
        for p in piles:
            heapq.heappush(pq, -p) #largest item to the top of heap, as smallest
        for i in range(k): #get the smallest item curr from the heap, and deduct curr//2 per requirement
            curr = heapq.heappop(pq)
            deduction = abs(curr)//2
            total -= deduction
            heapq.heappush(pq,  -(abs(curr) - deduction)) #push the rest back to the heap
        return total

