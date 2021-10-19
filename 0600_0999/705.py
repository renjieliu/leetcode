class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def add(self, key: int) -> None:
        if key >= len(self.arr):
            self.arr += [None] * (key - len(self.arr) + 1)
        self.arr[key] = key

    def remove(self, key: int) -> None:
        if key < len(self.arr):
            self.arr[key] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key < len(self.arr) and self.arr[key] != None:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)