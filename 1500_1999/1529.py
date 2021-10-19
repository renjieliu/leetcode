class Solution:
    def minFlips(self, target: str) -> int:
        arr = target.split('0')
        t = 0
        for a in arr:
            t += 1 if a and a[0] == '1' else 0

        if t == 0:
            return 0
        else:
            if target[-1] == '0':  # need to flip one more time for the last bulbs
                return 1 + t * 2 - 1
            else:
                return t * 2 - 1

