class Solution:
    def allPathsSourceTarget(self, graph: 'List[List[int]]') :
        def dfs(graph, curr_pos, curr_path, output):
            if curr_pos == len(graph) - 1:  # it has reached the end of the array
                output.append(curr_path)
            elif graph[curr_pos] == []:  # in the middle of the array, and it's blank, return.
                return []
            else:
                for i in range(len(graph[curr_pos])):  # iterate thru the curr node
                    nxt_pos = graph[curr_pos][i]
                    dfs(graph, nxt_pos, curr_path + [nxt_pos], output)
                return output

        return dfs(graph, 0, [0], [])  # start from position 0