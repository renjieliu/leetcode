class Vector2D:

    def __init__(self, v: 'List[List[int]]'):
        def flat(recr, stk):
            while recr:
                curr = recr.pop(0)
                if isinstance(curr, list):
                    if len(curr) > 0:
                        flat(curr, stk)
                else:
                    stk.append(curr)

        recr = v.copy()
        self.stk = []
        while recr:
            flat(recr.pop(0), self.stk)

    def next(self) -> int:
        return self.stk.pop(0)

    def hasNext(self) -> bool:
        return True if self.stk else False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()