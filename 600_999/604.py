class StringIterator:

    def __init__(self, compressedString: str):
        if compressedString == "":
            self.stk = []
        else:
            self.stk = [[compressedString[0], 0]]
            cnt = ""
            for i, c in enumerate(compressedString[1:]):
                if 48 <= ord(c) <= 57:
                    cnt += c
                else:
                    self.stk[-1][1] = int(cnt)  # since it has been added once, so it's cnt-1 times.
                    self.stk.append([c, 0])
                    cnt = ""
            self.stk[-1][1] = int(cnt)
            # print(self.stk)

    def next(self) -> str:
        if self.stk:
            ans = self.stk[0][0]
            self.stk[0][1] -= 1
            if self.stk[0][1] == 0:
                self.stk.pop(0)
            return ans
        else:
            return ' '

    def hasNext(self) -> bool:
        return True if self.stk else False

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()