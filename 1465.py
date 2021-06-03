class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: 'List[int]', verticalCuts: 'List[int]') -> int:
        mod = 10**9 + 7
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        arr_1 = []
        for i in range(1, len(horizontalCuts)):
            arr_1.append(horizontalCuts[i] - horizontalCuts[i-1])
        arr_2 = []
        for i in range(1, len(verticalCuts)):
            arr_2.append(verticalCuts[i] - verticalCuts[i-1])
        return max(arr_1) * max(arr_2) % mod

