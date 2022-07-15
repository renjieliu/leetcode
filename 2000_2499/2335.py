class Solution:
    def fillCups(self, amount: 'List[int]') -> int:
        pq = []
        for a in amount: 
            if a != 0:
                heapq.heappush(pq, -a)
        cnt = 0 
        while pq and len(pq) >1: # always take out 2 cups each time. 
            cnt += 1 
            a = -heapq.heappop(pq)
            b = -heapq.heappop(pq)
            a-=1 
            b-=1 
            if a > 0: 
                heapq.heappush(pq, -a)
            if b > 0:
                heapq.heappush(pq, -b)
            
            # print(pq)
            
        if len(pq) == 1: # if cannot take out 2 cups, fill the remainig cup with abs(pq[0]) seconds
            cnt += abs(pq[0])
        
        return cnt
    

    
    
