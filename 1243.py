class Solution:
    def transformArray(self, arr: 'List[int]') :
        if len(arr) in [1, 2]:
            return arr
        else:
            prev = arr.copy()
            curr = [None] * len(prev)
            while True:
                i = 0
                while i < len(arr):
                    if i in [0, len(prev) - 1]:
                        curr[i] = prev[i]
                    else:
                        if prev[i] < prev[i + 1] and prev[i] < prev[i - 1]:
                            curr[i] = prev[i] + 1
                        elif prev[i] > prev[i + 1] and prev[i] > prev[i - 1]:
                            curr[i] = prev[i] - 1
                        else:
                            curr[i] = prev[i]
                    i += 1
                if curr == prev:
                    return curr
                else:
                    prev = curr.copy()


