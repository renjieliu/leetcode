class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        for c, r in prerequisites:
            if c not in pre:
                pre[c] = []
            pre[c].append(r)

        def dfs(path, pre, c, checked):
            if c in path:
                return False
            else:
                if c in pre:
                    for x in pre[c]:
                        if dfs(path + [c], pre, x, checked) == False:
                            return False
                checked[c] = 1
                return True

        checked = [-1 for _ in range(numCourses)]

        for i in range(numCourses):
            if checked[i] == -1 and dfs([], pre, i, checked) == False:
                return False
        return True

#OLD Approach
# def dfs(graph, s, status):
#     if status[s] == 1: #cycle
#         return -1
#     elif status[s] == 2: #visited, and no cycle
#         return 1
#     else:
#         status[s] = 1
#         for x in graph[s]:
#             if dfs(graph, x, status) == -1:
#                 return -1
#
#         status[s] = 2
#
#     return 1
#
#
# def canFinish(numCourses: int, prerequisites: 'List[List[int]]'):
#     courses = {_:[] for _ in range(numCourses)}
#     for i, j in prerequisites:
#         courses[i].append(j)
#
#
#     status = [0] * numCourses
#
#     for i in courses:
#         if dfs(courses, i, status) == -1:
#             return False
#
#     return True
#
# print(canFinish(2, [[1,0],[0,1]]))
# print(canFinish(2, [[1,0]]))