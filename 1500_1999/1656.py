class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.arr = [None] * (n + 1)

    def insert(self, id: int, value: str) -> 'List[str]':
        self.arr[id] = value
        output = []
        if id == self.ptr:
            for i in range(self.ptr, len(self.arr)):
                if self.arr[i] != None:
                    output.append(self.arr[i])
                else:
                    self.ptr = i
                    break
            return output
