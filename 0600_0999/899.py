class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:  # try all the possible movements
            arr = []
            for i in range(len(s)):
                arr.append(s[i:] + s[:i])
            return min(arr)
        else:  # it can always find a way to be fully sorted
            return "".join(sorted(list(s)))

