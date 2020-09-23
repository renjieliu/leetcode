class Solution:
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> int:
        length = len(gas)
        gas = gas + gas
        cost = cost + cost

        for i in range(len(gas)):
            currGas = 0
            startOver = 0
            rem = 0
            for j in range(i, i + length):
                currGas = rem + gas[j]
                rem = currGas - cost[j]
                if rem < 0:
                    startOver = 1
                    break
            if startOver == 0:
                return i

            if i >= length:
                return -1