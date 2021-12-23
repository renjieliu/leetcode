class Solution:
    def findOrder(self, numCourses: int, prerequisites: 'List[List[int]]') -> 'List[int]':
        lkp = set(tuple(sorted(p)) for p in prerequisites)
        if len(lkp) != len(prerequisites):
            return []
        follow = {} 
        pre = {} 
        for b, a in prerequisites:
            if a not in follow: #b follows a
                follow[a] = set()
            follow[a].add(b)
            
            if b not in pre: #in order to take b, you need to take a first
                pre[b] = set()
            pre[b].add(a)
        
        leaf = [i for i in range(numCourses) if i not in follow] # the one without any followers, meaning they should be the last to take
        output = []
        seen = set()
        if leaf == []: # it's a loop
            return []
        else:
            while leaf: #BFS from the leaf to root, and return the output in reverse order
                nxt = []
                while leaf:
                    take = leaf.pop()
                    output.append(take)
                    seen.add(take)

                    if take in pre:
                        for f in pre[take]: #all the pre courses for current
                            if len(follow[f]) == 1:
                                nxt.append(f)
                                del follow[f]
                            else:
                                follow[f].remove(take)
    
                
                leaf = nxt
            
            return output[::-1] if len(output) == numCourses else [] # we added the leaf level first, so the output need to be reversed
        


# previous approach
# def dfs(courses, i, status, currentPath):
#     if status[i] == 1:
#         return -1
#     elif status[i] == 2:
#         return 1
#     else:
#         for x in courses[i]:
#             if dfs(courses, x, status, currentPath) == -1:
#                 return -1

#         currentPath.append(i)
#         status[i] = 2

#         return 1





# def findOrder( numCourses: int, prerequisites: 'List[List[int]]'):
#     courses = {_:[] for _ in range(numCourses)}

#     for i, j in prerequisites:
#         courses[i].append(j)
#     status = [0]*numCourses
#     output= []

#     for i in courses:
#         currentPath = []
#         if dfs(courses, i, status, currentPath) == -1:
#             return []


#         for i in currentPath:
#             output.append(i)

#     return output






# # print(findOrder(2, [[1,0]] ))
# # print(findOrder(2, [[1,0],[0,1]] ))
# print(findOrder(4, [[0,1], [0,2], [1,3],[2,3]]))
# print(findOrder(2, [[0,1]] ))

# # print(findOrder(6, [[1,0],[2,0],[3,1],[3,2]] ))
# # print(findOrder(3, [[2,0],[2,1]] ))
# # print(findOrder(3, [[0,1],[0,2],[1,2]]))
# # print(findOrder(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])) #[]
# #
# #

# previous approach

# class Solution:
#     def dfs(self, graph, s, status, currentPath):
#         if status[s] == 1:
#             return -1
#         elif status[s] ==2:
#             return 1
#         else:
#             status[s] =1
#             for g in graph[s]:
#                 if self.dfs(graph, g , status, currentPath) ==-1:
#                     return -1
            
#             status[s] =2
#             currentPath.insert(0, s)
#             return 1         
            
    
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         courses = {_:[] for _ in range(numCourses)} 
#         for i , j in prerequisites:
#             courses[i].append(j) #to add j as it's dependant.
            
#         output = []
#         status = [0] * numCourses       
#         for c in courses:
#             currentPath = []
#             if self.dfs(courses, c, status, currentPath) ==-1:
#                 return []
            
#             for i in currentPath[::-1]:
#                 output.append(i)

        
#         return output