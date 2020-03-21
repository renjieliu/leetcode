class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(n):
            output = 0
            while n != 1:
                output += 1
                if n % 2 == 0:
                    n //= 2
                else:
                    n = n * 3 + 1
            return output

        hmp = {}
        for i in range(lo, hi + 1):
            hmp[i] = power(i)
        return list(sorted(hmp.keys(), key=lambda x: hmp[x]))[k - 1]
