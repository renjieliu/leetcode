class MRUQueue:

    def __init__(self, n: int):
        self.stk = [_ for _ in range(1,n+1)]

    def fetch(self, k: int) -> int:
        res = self.stk[k-1]
        self.stk = self.stk[:k-1] +  self.stk[k:] + [self.stk[k-1]]
        return res

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)