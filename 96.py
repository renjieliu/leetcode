class Solution:
    def numTrees(self, n: int) -> int:
        stk = [0] * (n + 1)
        stk[0], stk[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                stk[i] += stk[j - 1] * stk[i - j]
        return stk[-1]


