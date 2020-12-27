class Solution:
    def averageWaitingTime(self, customers: 'List[List[int]]') -> float:
        chef = 0  # when the chef will be available
        totalWait = 0
        for arrive, wait in customers:
            if chef <= arrive:
                totalWait += wait
                chef = (arrive + wait)  # the chef will be availabe at time s+e
            else:
                chef += wait
                totalWait += chef - arrive
        return totalWait / len(customers)


