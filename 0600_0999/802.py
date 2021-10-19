class Solution:
    def eventualSafeNodes(self, graph: 'List[List[int]]') -> 'List[int]':
        def addPoints(dict_in, path):
            for p in path:
                if p not in dict_in:
                    dict_in[p] = 0

        def dfs(graph, curr_pos, curr_path, bad_points, temp_good, good_points):
            if curr_pos in curr_path or curr_pos in bad_points:  # a loop has been found
                addPoints(bad_points, curr_path)
                return -1
            elif graph[
                curr_pos] == [] or curr_pos in good_points:  # it has reached the terminal and current path is good.
                addPoints(temp_good, curr_path)  # add current "good" points to the curr_path.
                return 1
            else:
                for i in range(len(graph[curr_pos])):  # go thru all the path from the curr node
                    nxt = graph[curr_pos][i]
                    if dfs(graph, nxt, curr_path + [curr_pos], bad_points, temp_good, good_points) == -1:
                        return -1
                addPoints(good_points, temp_good.keys())  # all the points in the processes are good.
                return 1

        output = []
        good_points = {}
        bad_points = {}

        for curr_pos in range(len(graph)):
            if graph[curr_pos] == []:  # add to the output directly
                good_points[curr_pos] = 0
                output.append(curr_pos)
            else:
                curr_path = []
                temp_good = {}
                if curr_pos in bad_points:
                    continue
                elif curr_pos in good_points:
                    output.append(curr_pos)
                elif dfs(graph, curr_pos, curr_path, bad_points, temp_good, good_points) == 1:
                    output.append(curr_pos)

        return output






