class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        replace = []
        rem = k - n  # assume all are "a"
        while rem > 0:
            nxt = min(rem, 25)  # "a" is 1, and it has already in place, hence the max can be added will be 25
            rem -= nxt
            replace.append(chr(97 + nxt))
        return "a" * (n - len(replace)) + "".join(sorted(replace))


