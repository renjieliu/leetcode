class Solution:
    def mergeSimilarItems(self, items1: 'List[List[int]]', items2: 'List[List[int]]') -> 'List[List[int]]': #O( NlogN | N )
        hmp = defaultdict(lambda: 0)
        for a, b in items1 + items2: #merge items1 and items2 
            hmp[a] += b 
        return [[k, hmp[k]] for k in sorted(hmp.keys())]
    

    
