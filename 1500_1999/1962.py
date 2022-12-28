class Solution:
    def minStoneSum(self, piles: 'List[int]', k: int) -> int: # O( NlogN | N )
        pq = []
        total = 0
        while piles: # build the min heap
            total += piles[-1]
            heapq.heappush(pq, -piles.pop()) 
        
        cnt = 0 
        while cnt < k: # greedy, keep taking out the smallest(largest) piles from the heap
            A = -heapq.heappop(pq) 
            total -= A//2 
            rem = A - A//2
            heapq.heappush(pq, -rem) # push the remaining back to the heap
            cnt += 1
            
        return total
            
        
        

# previous solution

# class Solution:
#     def minStoneSum(self, piles: 'List[int]', k: int) -> int:
#         pq = []
#         total = sum(piles)
#         for p in piles:
#             heapq.heappush(pq, -p) #largest item to the top of heap, as smallest
#         for i in range(k): #get the smallest item curr from the heap, and deduct curr//2 per requirement
#             curr = heapq.heappop(pq)
#             deduction = abs(curr)//2
#             total -= deduction
#             heapq.heappush(pq,  -(abs(curr) - deduction)) #push the rest back to the heap
#         return total

