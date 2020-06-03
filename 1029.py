class Solution:
    def twoCitySchedCost(self, costs: 'List[List[int]]') -> int:
        costs = sorted(costs, key = lambda x:x[0] - x[1])
        return sum(map(lambda x: x[0], costs[:len(costs)//2])) + sum(map(lambda x: x[1], costs[len(costs)//2:]))