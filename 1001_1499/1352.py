class ProductOfNumbers:

    def __init__(self):
        self.zeroPos = []
        self.prod = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prod.append(num)
            self.zeroPos.append(len(self.prod) - 1)  # the last zero position
        else:
            if self.prod == [] or self.prod[-1] == 0:
                self.prod.append(num)
            else:
                self.prod.append(self.prod[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.zeroPos != []:
            start = len(self.prod) - k
            if self.zeroPos[-1] >= start:  # the last zero is within the query range
                return 0
            elif self.zeroPos[-1] < start:  # zero before the range
                if k == len(self.prod[self.zeroPos[-1] + 1:]):  # k == arr[lastZero: ]
                    return self.prod[-1]
                else:
                    return self.prod[-1] // self.prod[-k - 1]

        elif self.zeroPos == []:  # no zero
            if k == len(self.prod):
                return self.prod[-1]
            else:
                return self.prod[-1] // self.prod[-k - 1]

            # Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)