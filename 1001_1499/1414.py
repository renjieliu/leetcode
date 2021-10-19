class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def fib(n):
            if n in [1, 2]:
                return 1
            else:
                n1 = 1
                n2 = 1
                i = 3
                while i <= n:
                    n3 = n1 + n2
                    n1 = n2
                    n2 = n3
                    i += 1
            return n3

        pool = []  # pool for all the fib number <= k
        i = 1
        while fib(i) <= k:
            pool.append(fib(i))
            i += 1
        if pool[-1] == k:
            return 1
        else:
            rem = k - pool[-1]
            cnt = 1
            while rem > 1:  # keep use the largest fib number. until 1 or nothing left
                while pool and pool[-1] > rem:
                    pool.pop()
                rem -= pool[-1]
                cnt += 1

            return cnt + 1 if rem == 1 else cnt