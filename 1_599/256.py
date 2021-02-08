class Solution:
    def minCost(self, costs: 'List[List[int]]') -> int:
        if costs == []:
            return 0
        dp = [costs[-1]] #
        i = len(costs)-2
        while i > -1:#top-down
            c = costs[i]
            a = min(c[0] + dp[-1][1], c[0] + dp[-1][2])
            b = min(c[1] + dp[-1][0], c[1] + dp[-1][2])
            c = min(c[2] + dp[-1][0], c[2] + dp[-1][1])
            dp.append([a,b,c])
            i-=1
        return min(dp[-1])