class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr=[a,b,c]
        arr.sort()
        cnt = 0
        while arr[0] != 0: #pick the least and most, and sort
            cnt += 1
            arr[0] -= 1
            arr[2] -= 1
            arr.sort()
        return cnt + min( arr[1], arr[2])