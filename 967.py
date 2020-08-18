class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> 'List[int]':
        output = []
        for i in range(1, 10):
            stk = [str(i)]
            while stk and len(stk[0]) < N:
                curr = stk.pop(0)
                if 0 <= int(curr[-1]) - K <= 9:
                    stk.append(curr + str(int(curr[-1]) - K))
                if 0 <= int(curr[-1]) + K <= 9:
                    stk.append(curr + str(int(curr[-1]) + K))
            for s in stk:
                if len(s) == N:
                    output.append(int(s))

        if N == 1:
            output.append(0)

        return sorted(list(set(output)))
