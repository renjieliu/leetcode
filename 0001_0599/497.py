import random

class Solution:

    def __init__(self, rects: 'List[List[int]]'):
        self.stk = rects
        self.weights = [(r[2] - r[0] + 1) * (r[3] - r[1] + 1) for r in
                        rects]  # count the points in the rec, and assign a weight.
        self.numRange = [self.weights[0]]
        for w in self.weights[1:]:
            self.numRange.append(self.numRange[-1] + w)

    def pick(self) -> 'List[int]':
        r = random.randint(0, self.numRange[
            -1])  # find a random number from all the points, and find the corresponding rect
        s = 0
        e = len(self.numRange)
        while s <= e:  # binary search to find which rec has been picked
            mid = (s + e) // 2
            if self.numRange[mid] >= r:
                res = mid
                e = mid - 1
            else:
                s = mid + 1

        rct = self.stk[res]

        x = random.randint(rct[0], rct[2])  # pick a random X value from the rec
        y = random.randint(rct[1], rct[3])  # pick a random Y value from the rec
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()