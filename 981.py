class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hash:
            self.hash[key] = {}

        self.hash[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hash:
            return ""

        latest = -float('inf')
        for i in self.hash[key].keys():
            if i <= timestamp:
                latest = max(latest, i)

        if latest == -float('inf'):
            return ""
        else:
            return self.hash[key][latest]





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)