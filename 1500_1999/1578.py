class Solution:
    def minCost(self, colors: str, neededTime: 'List[int]') -> int: # O( NlogN | N )
        output = 0
        pq = []
        heapq.heapify(pq)
        prev = colors[0]
        for i in range(1, len(colors)): # push all the consecutive same colors to the heap. 
            curr = colors[i]
            if curr == prev:
                if pq:
                    heapq.heappush(pq, neededTime[i])
                else: # new heap, need to push the previous and current to the heap
                    heapq.heappush(pq, neededTime[i-1])
                    heapq.heappush(pq, neededTime[i])
            else: 
                if pq: #find the smallest ones from the heap, and take them out
                    while len(pq) > 1:
                        output += heapq.heappop(pq)
                    heapq.heappop(pq)
            prev = colors[i]
        
        while len(pq) > 1: #check the tail
            output += heapq.heappop(pq)
            
        return output
    
    



    
