def dfs(k, graph, output=None):
    if output ==None:
        output = []
    output.append(k)
    for i in graph[k]:
        if i not in output:
           dfs(i, graph, output)

    return output



def canVisitAllRooms(rooms: 'List[List[int]]'):
    if len(rooms[0]) == 0 and len(rooms) == 1:
        return True
    if len(rooms[0]) ==0 :
        return False

    graph = {}
    for i in range(len(rooms)):
        graph[i]= []
        for j in range(len(rooms[i])):
            graph[i].append(rooms[i][j])

    total = sum([i for i in range(len(rooms))])

    if sum(dfs(0, graph)) != total:

        return False
    else:
        return True





print(canVisitAllRooms( [[1],[2],[3],[]]))
print(canVisitAllRooms( [[]]))
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))



