class Solution:
    def maxIceCream(self, costs: 'List[int]', coins: int) -> int:
        costs.sort()
        cnt = 0
        while costs and coins > 0:
            coins -= costs.pop(0)
            if coins >= 0:
                cnt += 1
        return cnt

