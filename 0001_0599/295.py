class MedianFinder: # RL 20221111 copied previous solution. O( NlogN | N )

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] 
        self.large = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (self.large[0] - self.small[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()





# previous solution

# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.small = []
#         self.large = []
#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
#         if len(self.large) < len(self.small):
#             heapq.heappush(self.large, -heapq.heappop(self.small))

#     def findMedian(self) -> float:
#         if len(self.large) > len(self.small):
#             return float(self.large[0])
#         return (self.large[0] - self.small[0]) / 2.0



# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()