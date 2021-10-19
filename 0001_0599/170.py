class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmp = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.hmp:
            self.hmp[number] = 0
        self.hmp[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k, v in self.hmp.items():# same number can be added twice or different numbers
            if (value == k * 2 and v > 1) or (value != k * 2 and value - k in self.hmp):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)