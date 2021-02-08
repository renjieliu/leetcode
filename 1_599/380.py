import random;


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmp = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hmp:
            self.hmp[val] = None
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hmp:
            del self.hmp[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        k = list(self.hmp.keys())
        return k[random.randint(0, len(k) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()