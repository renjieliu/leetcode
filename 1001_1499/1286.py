class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def combo(output, curr, arr, target):
            if len(curr) == target:
                output.append(curr)
            else:
                for i in range(len(arr)):
                    combo(output, curr+arr[i], arr[i+1:], target)
        self.stk = []
        combo(self.stk, "", list(characters), combinationLength)
        self.ptr = 0

    def next(self) -> str:
        res = self.stk[self.ptr]
        self.ptr+=1
        return res

    def hasNext(self) -> bool:
        return self.ptr<len(self.stk)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()