class Solution:
    def processQueries(self, queries: 'List[int]', m: int) -> 'List[int]':
        perm = [_ for _ in range(1, m+1)] 
        output = []
        for q in queries:
            i = 0 
            while i < len(perm):
                if perm[i] == q:
                    output.append(i)
                    perm = [perm[i]] + perm[:i] + perm[i+1:]
                    break                
                i+=1
        return output