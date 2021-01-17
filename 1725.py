class Solution:
    def countGoodRectangles(self, rectangles: 'List[List[int]]') -> int:
        hmp = defaultdict(int)
        for w, l in rectangles:
            hmp[min(w,l)] += 1
        return hmp[max(hmp.keys())]