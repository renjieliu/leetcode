class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + 2*i)
        output = arr[0]
        for a in arr[1:]:
            output ^= a
        return output