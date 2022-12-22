class Solution:
    def canVisitAllRooms(self, rooms: 'List[List[int]]') -> bool: # O( N | N )
        visited = set()
        stk = [0] 
        while stk: # BFS to visit all the possible rooms from curr.
            nxt = [] 
            while stk:
                curr = stk.pop()
                visited.add(curr)  # not previously visited
                for _ in rooms[curr]:
                    if _ not in visited:
                        nxt.append(_)
            stk = nxt
        
        return len(visited) == len(rooms)




# previous solution 

# class Solution:
#     def canVisitAllRooms(self, rooms: 'List[List[int]]') -> bool:
#         def dfs(seen, arr, curr):
#             for c in arr[curr]:
#                 if c not in seen:
#                     seen.add(c)
#                     dfs(seen, arr, c)
#         seen = set([0])
#         dfs(seen, rooms,0)
#         #print(seen)
#         return len(seen) == len(rooms)




# previous solution

# class Solution:
#     def dfs(self, k, graph, output=None):
#         if output ==None:
#             output = []
#         output.append(k)
#         for i in graph[k]:
#             if i not in output:
#                 self.dfs(i, graph, output)

#         return output


    
    
    
#     def canVisitAllRooms(self, rooms: 'List[List[int]]') -> bool:
#         if len(rooms[0]) == 0 and len(rooms) == 1:
#             return True
#         if len(rooms[0]) ==0 :
#             return False

#         graph = {}
#         for i in range(len(rooms)):
#             graph[i]= []
#             for j in range(len(rooms[i])):
#                 graph[i].append(rooms[i][j])

#         total = sum([i for i in range(len(rooms))])

#         if sum(self.dfs(0, graph)) != total:

#             return False
#         else:
#             return True



