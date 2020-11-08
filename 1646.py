class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            arr = [-1] * (n + 1)
            arr[0] = 0
            arr[1] = 1
            for i in range(2, n + 1):
                if i % 2 == 0:
                    arr[i] = arr[i // 2]
                else:
                    arr[i] = arr[i // 2 + 1] + arr[i // 2]
            return max(arr)
