class Solution:
    def numWays(self, s: str) -> int:
        mod = 10 ** 9 + 7
        pos = []
        for i, c in enumerate(s):
            if c == "1":
                pos.append(i)
        if len(pos) % 3 != 0:
            return 0
        elif len(pos) == 0:  # Combination of n pick 2.
            fact = lambda x: x * (fact(x - 1) if x > 1 else 1)
            total = len(s) - 1
            pick = 2
            return (fact(total) // (fact(total - pick) * fact(pick))) % mod

        else:
            target = len(pos) // 3  # number of 1 in each partition
            cnt = 0
            while cnt < target:
                loc1 = pos.pop(0)
                cnt += 1
            cnt = 0
            while cnt < target:
                loc2 = pos.pop()
                cnt += 1

            a1 = pos[0] - loc1
            a2 = loc2 - pos[-1]
            return (a1 * a2) % mod

