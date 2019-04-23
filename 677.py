class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def insert(self, key: str, val: int) -> None:
        self.hash[key] = val

    def sum(self, prefix: str) -> int:
        output = 0
        for k, v in self.hash.items():
            if k.find(prefix) == 0:
                output += v
        return output

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)