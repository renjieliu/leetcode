class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minTrack = []
        self.minn = float('inf')

    def push(self, x: int) -> None:
        self.stk.append(x)
        if x == self.minn:
            self.minTrack[-1][x] += 1
        elif x < self.minn:
            self.minTrack.append({x: 1})
        self.minn = min(self.minn, x)

    def pop(self) -> None:
        x = self.stk[-1]
        if x == list(self.minTrack[-1].keys())[0]:  # same as the last value of the track stack
            self.minTrack[-1][x] -= 1
            if self.minTrack[-1][x] == 0:
                self.minTrack.pop(-1)
                if len(self.minTrack) > 0:
                    self.minn = list(self.minTrack[-1].keys())[0]

        self.stk.pop(-1)

        if len(self.stk) == 0 or len(self.minTrack) == 0:
            self.stk = []
            self.minTrack = []
            self.minn = float('inf')

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return list(self.minTrack[-1].keys())[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()