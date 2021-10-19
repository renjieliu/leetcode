class FirstUnique:

    def __init__(self, nums: 'List[int]'):
        self.hmp = {}
        self.stk = []
        for n in nums:
            if n not in self.hmp:
                self.hmp[n] = 0
            self.hmp[n] += 1
            if self.hmp[n] == 1:
                self.stk.append(n)
            while self.stk and self.hmp[self.stk[0]] > 1:
                self.stk.pop(0)

    def showFirstUnique(self) -> int:
        if self.stk:
            return self.stk[0]
        return -1

    def add(self, value: int) -> None:
        if value not in self.hmp:
            self.hmp[value] = 0
        self.hmp[value] += 1
        if self.hmp[value] == 1:
            self.stk.append(value)

        while self.stk and self.hmp[self.stk[0]] > 1:
            self.stk.pop(0)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)