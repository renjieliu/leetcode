class ZigzagIterator:
    def __init__(self, v1: 'List[int]', v2: 'List[int]'):
        self.stk = []
        if v1 and v2:
            self.stk = [v1, v2]
        elif v1:
            self.stk = [v1]
        elif v2:
            self.stk = [v2]
        self.pos = 0

    def next(self) -> int:
        if self.stk:
            ans = self.stk[self.pos].pop(0)
            if self.stk[self.pos] == []:
                self.stk = self.stk[:self.pos] + self.stk[self.pos + 1:]
                if self.pos == (len(self.stk) + 1) - 1:  # the last index of the stk before pop
                    self.pos = 0
            else:
                self.pos = (self.pos + 1) % len(self.stk)

            return ans

    def hasNext(self) -> bool:
        return True if self.stk else False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())