#reservoir sampling

import random
class Solution:
    def __init__(self, nums: 'List[int]'):
        self.nums = nums
    def pick(self, target: int) -> int:
        cnt = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                cnt+=1
                k = random.randint(0, cnt-1)
                if k==0:
                    output = i
        return output

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,3,3])
param_1 = obj.pick(3)
print(param_1)

