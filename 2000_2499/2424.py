class LUPrefix:

    def __init__(self, n: int): 
        self.valid = 0
        self.pq = []
        heapq.heapify(self.pq)
        self.cnt = 0
        

    def upload(self, video: int) -> None: # O( logN | N )
        heapq.heappush(self.pq, video)
        

    def longest(self) -> int: # O( logN | 1 )
        if (len(self.pq) == 0 and self.cnt == 0) or (self.pq and self.pq[0] != 1 and self.valid == 0): # if no element in the pq, it 1 is never seen, and current first element is also not 1
            return 0 
        else: 
            if self.pq and self.pq[0] == 1: # start counting
                self.valid = 1
            while self.pq and self.pq[0] == self.cnt + 1: #see if current and previous is continuous
                self.cnt = heapq.heappop(self.pq)
           
            return self.cnt

            
            



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
