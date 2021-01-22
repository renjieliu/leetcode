class Solution:
    def grayCode(self, n: int) -> 'List[int]':
        prev = ["0", "1"]
        for i in range(2, n + 1):  # each time, add 0 in the front of prev, and add 1 in the front in reverse order
            curr = []
            for p in prev:
                curr.append("0" + p)
            for p in prev[::-1]:
                curr.append("1" + p)
            prev = curr

        return [int(p, 2) for p in prev]
