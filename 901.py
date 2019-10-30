class StockSpanner:
    def __init__(self):
        self.stk = []
        self.rem = []

    def next(self, price: int) -> int:
        self.stk.append(price)
        self.rem.append(1)
        # below is to crash the stk and return the final result
        while self.rem:
            if len(self.rem) == 1:
                break
            else:
                if self.stk[-2] <= self.stk[-1]:
                    self.stk[-2] = self.stk[-1]
                    self.stk.pop()
                    self.rem[-1] += self.rem[-2]
                    self.rem[-2] = self.rem[-1]
                    self.rem.pop()
                else:
                    break

        return self.rem[-1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)