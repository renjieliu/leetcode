class Solution:
    def maxDistance(self, arrays: 'List[List[int]]') -> int:
        maxx, minn = -float('inf'), float('inf')
        loc = -1
        for i, a in enumerate(arrays):
            maxx = max(maxx, a[-1])
            minn = min(minn, a[0])
            if maxx == a[-1] and minn == a[0]:  # same array
                loc = i

        if loc == -1:
            return abs(maxx - minn)
        else:
            output = -float('inf')
            for i, a in enumerate(arrays):
                if i != loc:
                    output = max(output, abs(a[-1] - minn))
                    output = max(output, abs(a[0] - maxx))
            return output