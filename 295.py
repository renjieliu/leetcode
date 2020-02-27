class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        if self.arr == []:
            self.arr.append(num)
        else:  # binary search to find the insert point
            if num > self.arr[-1]:
                self.arr.append(num)
            elif num < self.arr[0]:
                self.arr = [num] + self.arr
            else:
                s = 0
                e = len(self.arr) - 1
                while s <= e:
                    mid = s - (s - e) // 2
                    if self.arr[mid] > num:
                        e = mid - 1
                    elif self.arr[mid] == num:
                        s = mid
                        break
                    elif self.arr[mid] < num:
                        s = mid + 1
                if num <= self.arr[s]:
                    self.arr = self.arr[:s] + [num] + self.arr[s:]
                else:
                    self.arr = self.arr[:s + 1] + [num] + self.arr[s + 1:]

    def findMedian(self) -> float:
        # print(self.arr)
        if len(self.arr) == 1:
            return self.arr[0]
        elif len(self.arr) % 2 == 0:
            return (self.arr[(len(self.arr) - 1) // 2] + self.arr[len(self.arr) // 2]) / 2
        else:
            return self.arr[len(self.arr) // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()