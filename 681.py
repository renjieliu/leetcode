class Solution:
    def nextClosestTime(self, time: str) -> str:
        compare = set(time)
        arr = []
        for i in range(24):
            for j in range(60):
                h = ('0' if i < 10 else '') + str(i)
                m = ('0' if j < 10 else '') + str(j)
                arr.append(h + ':' + m)

        candidate = []
        for a in arr:
            if len(set(a) - compare) == 0:
                candidate.append(a)
        candidate.sort()
        for c in candidate:
            if c > time:
                return c
        return candidate[0]

