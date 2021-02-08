"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, hmp):
            for n in node.neighbors:
                if n not in hmp:
                    hmp[n] = Node(n.val)
                    dfs(n, hmp)
                hmp[node].neighbors.append(hmp[n])


        if node == None:
            return None
        hmp = { node: Node(node.val) }
        dfs(node, hmp)
        return hmp[node]



