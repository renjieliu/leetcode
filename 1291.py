class Solution:
    def sequentialDigits(self, low: int, high: int) -> 'List[int]':
        def add(curr, high, output):
            if int(curr) < high:
                output.append(curr)
                if int(curr[-1])<9:
                    curr+= str(int(curr[-1]) + 1)
                    add(curr, high, output)
        output = []
        for i in range(1, 10):
            add(str(i), high, output)
        res = []
        for o in output:
            if low <= int(o) <= high :
                res.append(int(o))
        return sorted(res)