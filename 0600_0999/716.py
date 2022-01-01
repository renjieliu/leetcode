class MaxStack:

    def __init__(self):
        self.stk = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def peekMax(self) -> int:
        return max(self.stk)

    def popMax(self) -> int:
        m = max(self.stk)
        for i in range(len(self.stk)-1,-1,-1):
            if self.stk[i] == m:
                self.stk = self.stk[:i] + self.stk[i+1:]
                break
        # print(self.stk)
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

