class SmallestInfiniteSet:

    def __init__(self): #O( 1 | N )
        self.n = 1
        self.pq = []
        heapq.heapify(self.pq)
        self.pq_set =set() # record all the numbers in the pq
        

    def popSmallest(self) -> int: #O( 1 | 1 )
        if self.pq: # smaller number in the heap
            output = heapq.heappop(self.pq)
            self.pq_set.remove(output)
        else:
            output = self.n #if no heap, return current pointer
            self.n += 1 

        return output
            
        

    def addBack(self, num: int) -> None: #O( logN | N)
        if num not in self.pq_set and num < self.n: #no need to add, if num is already added back, or >= pointer
            heapq.heappush(self.pq, num)
            self.pq_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


