class Solution:
    def findContestMatch(self, n: int) -> str:
        stk = [str(_) for _ in range(1, n + 1)]
        while len(stk) > 2:  # keep popping the last element from the array and add to the current element
            i = 0
            while i < len(stk):
                stk[i] = "(" + stk[i] + "," + stk.pop() + ")"
                i += 1
        output = "(" + stk[0] + "," + stk[1] + ")"
        return output
