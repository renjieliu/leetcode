class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmp = {}  # to store the key loc in the stk
        self.used = []

    def get(self, key: int) -> int:
        if key not in self.hmp:
            return -1
        else:  # mark current one is used
            pos = -1
            for i, c in enumerate(self.used):
                if c == key:
                    pos = i
                    break
            self.used = self.used[:pos] + self.used[pos + 1:] + [key]

            return self.hmp[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hmp:
            for i, c in enumerate(self.used):
                if c == key:
                    pos = i
                    break
            self.used = self.used[:pos] + self.used[pos + 1:] + [key]
            self.hmp[key] = value
        else:
            if len(self.hmp) == self.capacity:  # if used all of them.
                del self.hmp[self.used[0]]  # the first one is least recent used
                self.used.pop(0)

            self.used.append(key)
            self.hmp[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)