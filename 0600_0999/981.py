class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hash:
            self.hash[key] = {}
            self.hash[key][-2] = timestamp  # used to store the lowest value

        self.hash[key][timestamp] = value
        self.hash[key][-1] = timestamp  # used to store the latest value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hash:
            return ""

        latest = self.hash[key][-1]
        lowest = self.hash[key][-2]

        if timestamp >= latest:
            return self.hash[key][latest]

        elif timestamp == lowest:
            return self.hash[key][lowest]

        elif timestamp < lowest:
            return ""


        else:
            for i in range(timestamp, -1, -1):
                if i in self.hash[key]:
                    return self.hash[key][i]

        # latest = -float('inf')
        # for i in self.hash[key].keys():
        #     if i<=timestamp:
        #         latest = max(latest, i)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)