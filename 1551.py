class Solution:
    def minOperations(self, n: int) -> int:
        total = [2 * i + 1 for i in range(n)]
        avg = sum(total) // n
        output = 0
        for t in total:
            if t < avg:
                output += avg - t
            else:
                return output
