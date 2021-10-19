class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1: return n
        arr = [_ for _ in range(1, n + 1)]
        move = 1
        pos = 0
        while True:
            if move % k == 0:
                arr = arr[:pos] + arr[pos + 1:]  # clean up the array
                move += 1  # after cleanup, walk ahead, but the position stays the same.
                if len(arr) == 1:
                    return arr[0]
            else:
                pos += 1
                pos = pos % len(arr)
                move += 1
