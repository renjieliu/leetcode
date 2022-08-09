class Solution:
    def reachableNodes(self, n: int, edges: 'List[List[int]]', restricted: 'List[int]') -> int: #O( N | N )
        def dfs(hmp, reached, curr, seen, restricted): #from current node, to reach as many as possible.
            for n in hmp[curr]:
                if n not in restricted and n not in seen and n not in reached: # if the node is in reached or seen already, no need to dfs again.
                    reached.add(n)
                    seen.add(n)
                    dfs(hmp, reached, n, seen, restricted)
                    seen.remove(n)
        
        hmp = defaultdict(lambda: []) # record all the neighbours
        for a, b in edges: #
            hmp[a].append(b)
            hmp[b].append(a)
        
        restricted = set(restricted)
        
        if 0 in restricted:
            return 0 
        else:
            reached = {0}
            seen = {0}
            dfs(hmp, reached, 0, seen, restricted)
            return len(reached)
    
