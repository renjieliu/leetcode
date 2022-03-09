class Solution:
    def getAncestors(self, n: int, edges: 'List[List[int]]') -> 'List[List[int]]':
        hmp = {_:[] for _ in range(n)}
        for f , t in edges: #for each node, add the parent of current edge
            hmp[t].append(f)
        output = [set() for _ in range(n)]  #using set to avoid the same "from" being added multiple times
        
        def dfs(seen, output, hmp, node):
            for nxt in hmp[node]: #for node, add all the direct from
                output[node].add(nxt) 
                if nxt not in seen:
                    seen.add(nxt)
                    output[node] |= dfs(seen, output, hmp, nxt) # add all the direct from of the "from"
                else:
                    output[node] |= output[nxt] 

            return output[node]
        
        # print(hmp)
        seen = set()
        for i in range(n):
            dfs(seen,output, hmp, i)
        
        return [sorted(list(_)) for _ in output] #deduplicate each one and sort, per requirement
    

    
    