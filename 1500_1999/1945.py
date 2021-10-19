class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ''.join([str(ord(c) - ord('a')+ 1) for c in s])
        while k > 0:
            t = sum([int(_) for _ in list(str(t))])
            k-= 1
        return t

