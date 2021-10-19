class Solution:
    def countPoints(self, points: 'List[List[int]]', queries: 'List[List[int]]') -> 'List[int]':
        good = lambda x, q: 1 if ( x[0] - q[0] ) ** 2 + ( x[1] - q[1] ) ** 2 <= q[2]**2 else 0
        output = []
        for q in queries:
            cnt = 0
            for p in points:
                cnt += 1 if good(p, q) == 1 else 0
            output.append(cnt)
        return output

