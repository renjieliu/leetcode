def dfs(courses, i, status, currentPath):
    if status[i] == 1:
        return -1
    elif status[i] == 2:
        return 1
    else:
        for x in courses[i]:
            if dfs(courses, x, status, currentPath) == -1:
                return -1

        currentPath.append(i)
        status[i] = 2

        return 1





def findOrder( numCourses: int, prerequisites: 'List[List[int]]'):
    courses = {_:[] for _ in range(numCourses)}

    for i, j in prerequisites:
        courses[i].append(j)
    status = [0]*numCourses
    output= []

    for i in courses:
        currentPath = []
        if dfs(courses, i, status, currentPath) == -1:
            return []


        for i in currentPath:
            output.append(i)

    return output






# print(findOrder(2, [[1,0]] ))
# print(findOrder(2, [[1,0],[0,1]] ))
print(findOrder(4, [[0,1], [0,2], [1,3],[2,3]]))
print(findOrder(2, [[0,1]] ))

# print(findOrder(6, [[1,0],[2,0],[3,1],[3,2]] ))
# print(findOrder(3, [[2,0],[2,1]] ))
# print(findOrder(3, [[0,1],[0,2],[1,2]]))
# print(findOrder(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])) #[]
#
#


