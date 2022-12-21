class Solution:
    def possibleBipartition(self, n: int, dislikes: 'List[List[int]]') -> bool: # O( N | N )
        people = defaultdict(lambda : []) # group all the disliked people
        for p, dis in dislikes:
            people[p].append(dis)
            people[dis].append(p)
        
        def dfs(color, people, curr, n): 
            if curr in color:
                return color[curr] == n
            color[curr] = n 
            for nxt in people[curr]:
                if dfs(color, people, nxt, n^1) == False :
                    return False 
            
            return True 
    
        color = {}
        for k, v in people.items():
            if k not in color:
                if dfs(color, people, k, 0) == False: # initially put the root to 0, and check if everyone disliked is 1
                    return False 
            
        return True



# previous solution

# class Solution:
#     def possibleBipartition(self, N: int, dislikes: 'List[List[int]]') -> bool:
#         hmp = {}
#         for d in dislikes:
#             if d[0] not in hmp: hmp[d[0]] = []
#             if d[1] not in hmp: hmp[d[1]] = []
#             hmp[d[0]].append(d[1])
#             hmp[d[1]].append(d[0])

#         placed = {}

#         def dfs(placed, hmp, n, level):
#             if n in placed:
#                 return level == placed[n]  # to check if it's in the right place
#             else:
#                 placed[n] = level
#                 if n in hmp:
#                     for c in hmp[n]:
#                         if dfs(placed, hmp, c, level ^ 1) == False:
#                             return False
#                 return True

#         for i in range(1, N + 1):
#             if i not in placed:  # has not placed yet.
#                 if dfs(placed, hmp, i, 0) == False:
#                     return False
#         return True



# previous solution


# class Solution:
#     def possibleBipartition(self, N: int, dislikes: 'List[List[int]]') -> bool:
#         if dislikes == []: return True
#         hmp = {} 
#         for a, b in dislikes: #build hmp for fast lookup
#             if a not in hmp: hmp[a] = []
#             if b not in hmp: hmp[b] = []
#             hmp[a].append(b)
#             hmp[b].append(a)

#         pool = {}
#         def dfs(node, c):
#             if node in pool:
#                 return pool[node] == c
#             pool[node] = c
#             if node in hmp:
#                 for x in hmp[node]:
#                     if dfs(x, c^1) == False:
#                         return False
#             return True
            
#         for node in range(1, N+1):
#             if node not in pool:
#                 if dfs(node, 0) == False:
#                      return False
#         return True
    