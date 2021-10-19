class Solution:
    def createSortedArray(self, instructions: 'List[int]') -> int:
        # implement Binary Index Tree
        def update(index, value, bit, m):
            index += 1
            while index < m:
                bit[index] += value
                index += index & -index

        def query(index, bit):
            index += 1
            result = 0
            while index >= 1:
                result += bit[index]
                index -= index & -index
            return result

        MOD = 10**9+7
        m = max(instructions)+2
        bit = [0]*m
        cost = 0

        n = len(instructions)
        for i in range(n):
            left_cost = query(instructions[i]-1, bit)
            right_cost = i - query(instructions[i], bit)
            cost += min(left_cost, right_cost)
            update(instructions[i], 1, bit, m)
        return cost % MOD