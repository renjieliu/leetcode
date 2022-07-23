class Solution:
    def leadsToDestination(self, n: int, edges: 'List[List[int]]', source: int, destination: int) -> bool: # O( N | N )
        hmp = {}
        for f, t in edges:
            if f not in hmp:
                hmp[f] = []
            hmp[f].append(t) 
            
        if destination in hmp: #destination should not have next nodes
            return False 
    
        def dfs(hmp, dp, seen, destination, curr): #check all the posibilities, and see if it can reach end 
            if curr in dp:
                return dp[curr]
            else:
                if curr == destination:
                    dp[curr] = 1 
                elif curr not in hmp:
                    dp[curr] = 0
                else:  
                    dp[curr] = 1
                    for nxt in hmp[curr]:
                        if nxt not in seen:
                            seen.add(nxt)
                            dp[curr] *= dfs(hmp, dp, seen, destination, nxt)
                            seen.remove(nxt)
                        else:
                            dp[curr] = 0 
                            break
                return dp[curr] 
        
        dp = {}
        dfs(hmp, dp, set(), destination, source)
        return dp[source]


                
                
                
              
                
                
# previous solution 

# class Solution:
#     def leadsToDestination(self, n: int, edges: 'List[List[int]]', source: int, destination: int) -> bool:
#         hmp = {}
#         for s, e in edges:
#             if s not in hmp:
#                 hmp[s] = []
#             if s == destination: #if current start is destination, then destination is not the last stop
#                 return False
#             hmp[s].append(e)


#         def helper(hmp, curr, destination, seen): #dfs to check if from source can reach destination
#             # print(curr)
#             if curr == destination:
#                 return 1
#             else:
#                 valid = 1
#                 for node in hmp[curr]:
#                     if node in seen or (node not in hmp and node!=destination):
#                         return 0
#                     elif node not in seen:
#                         seen.add(node)
#                         valid = helper(hmp, node, destination, seen)
#                         if valid == 0:
#                             return 0
#                         seen.remove(node)

#                 return valid == 1

#         if source == destination:
#             return True
#         elif source not in hmp:
#             return False
#         else:
#             # print(hmp)
#             return helper(hmp, source, destination, set())



