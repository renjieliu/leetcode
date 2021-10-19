class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.limit = maxSize

    def push(self, x: int) -> None:
        if len(self.stk) < self.limit:
            self.stk = [x] + self.stk

    def pop(self) -> int:
        if self.stk == []:
            return -1
        else:
            return self.stk.pop(0)

    def increment(self, k: int, val: int) -> None:
        if len(self.stk) <= k:
            i = 0
            while i < len(self.stk):
                self.stk[i] += val
                i += 1
        else:
            i = -k
            while i <= -1:
                self.stk[i] += val
                i += 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)