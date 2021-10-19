class Solution:
    def findCenter(self, edges: 'List[List[int]]') -> int:
        hmp = defaultdict(list)
        for a , b in edges:
            hmp[a].append(b)
            hmp[b].append(a)
        for k, v in hmp.items():
            if len(v) == len(hmp)-1:
                return k
