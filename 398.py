import random
class Solution:
    def __init__(self, nums: 'List[int]'):
        self.map = {}
        for i in range(len(nums)):
            if nums[i] not in self.map:
                self.map[nums[i]] = []
            self.map[nums[i]].append(i)

    def pick(self, target: int) -> int:
        start = 0
        end = len(self.map[target])-1
        k = random.randint(start, end)
        return self.map[target][k]

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,3,3])
param_1 = obj.pick(3)
print(param_1)

