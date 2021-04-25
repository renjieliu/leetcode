class Solution:
    def sumBase(self, n: int, k: int) -> int:
        output= 0
        while n > 0:
            output+= n%k
            n //= k
        return output
