class Solution:
    def destCity(self, paths: 'List[List[str]]') -> str:
        f, t = set(), set()
        for p in paths:
            f.add(p[0])
            t.add(p[1])
        return list(t-f)[0]