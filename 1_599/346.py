class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.stk = []
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.stk) >= self.size:
            self.total -= self.stk.pop(0)

        self.stk.append(val)
        self.total += val

        return self.total / len(self.stk)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)