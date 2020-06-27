class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1) if n % i == 0]
        return -1 if k > len(arr) else arr[k-1]