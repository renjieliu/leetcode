class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        r1 = [[A, B], [C, D]]
        r2 = [[E, F], [G, H]]
        s1 = abs(r1[1][0] - r1[0][0]) * abs(r1[1][1] - r1[0][1])
        s2 = abs(r2[1][0] - r2[0][0]) * abs(r2[1][1] - r2[0][1])
        if r2[0][0] >= r1[1][0] or r2[1][0] <= r1[0][0] or r2[0][1] >= r1[1][1] or r2[1][1] <= r1[0][
            1]:  # no overlapping
            return s1 + s2
        elif (r1[0][0] <= r2[0][0] <= r2[1][0] <= r1[1][0] and r1[0][1] <= r2[0][1] <= r2[1][1] <= r1[1][1]) \
                or (r2[0][0] <= r1[0][0] <= r1[1][0] <= r2[1][0] and r2[0][1] <= r1[0][1] <= r1[1][1] <= r2[1][
            1]):  # complete overlapping
            return max(s1, s2)
        else:  # partial overlapping
            x1 = max(r1[0][0], r2[0][0])  # for the left X, which is the max
            x2 = min(r1[1][0], r2[1][0])  # for the right X, which is the min
            x = abs(x2 - x1)
            y1 = max(r1[0][1], r2[0][1])  # for the lower y, which is the max
            y2 = min(r1[1][1], r2[1][1])  # for the upper y, which is the min
            y = abs(y2 - y1)
            return s1 + s2 - x * y

