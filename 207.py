def dfs(graph, s, done):
    if done[s] == 0:
        done[s] = 1
        for x in graph[s]:
            if dfs(graph, x, done) == -1:
                return -1
        done[s] = 2
        return 0

    elif done[s] == 1:  # it is being visited
        return -1

    elif done[s] == 2:  # it has been done before
        return 0


def canFinish(numCourses: int, prerequisites: 'List[List[int]]') -> bool:
    courses = {_: [] for _ in range(numCourses)}

    for i, j in prerequisites:
        courses[i].append(j)

    done = [0] * numCourses

    for i in courses:
        if dfs(courses, i, done) == -1:
            return False

    return True


print(canFinish(2, [[1,0]] ))
print(canFinish(2, [[1,0],[0,1]] ))
print(canFinish(3, [[0,1],[0,2],[1,2]] ))


