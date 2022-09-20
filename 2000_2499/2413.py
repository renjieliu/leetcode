class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * (n % 2+1)  # if n is even , return n itself. else, return n*2

