class Solution:
    def pickGifts(self, gifts: 'List[int]', k: int) -> int: # O( NlogN | N )
        pq = [-g for g in gifts] # create the heap
        heapq.heapify(pq)
        cnt = 0
        while cnt < k: 
            heapq.heappush(pq, -int( (-heapq.heappop(pq))**0.5 )) # take out max, and push back the floor(-mx**0.5)
            cnt += 1
        return sum(-p for p in pq) # return the total of remaining numbers
    


