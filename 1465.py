class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: 'List[int]', verticalCuts: 'List[int]') -> int:
        horizontalCuts = sorted([0] + horizontalCuts + [h])
        verticalCuts = sorted([0] + verticalCuts + [w])
        h_gap = [horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts))]
        v_gap = [verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts))]
        mod = 10 ** 9 + 7
        return max(h_gap) * max(v_gap) % mod  # adjacent max(h_gap)  * ajacent v_gap
