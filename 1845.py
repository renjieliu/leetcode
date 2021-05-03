class SeatManager:

    def __init__(self, n: int):
        self.heap = [] #store the unreserved seats
        heapq.heapify(self.heap)
        self.curr = 0

    def reserve(self) -> int:
        if len(self.heap) == 0 : #no seat has been unreserved
            self.curr+=1
            return self.curr
        else:
            res = heapq.heappop(self.heap) # get the seat was previously unreserved, with the smallest number
            return res


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber) #the seat is become available


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)