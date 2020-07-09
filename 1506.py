"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def findRoot(self, tree: 'List[\'Node\']') -> 'Node':
        hmp = {}
        for node in tree:
            if node.val not in hmp:
                hmp[node.val] = []
            for c in node.children:
                hmp[node.val].append(c.val)

        def dfs(node, hmp, dp):
            if node in dp:
                return dp[node]
            else:
                dp[node] = 1  # count itself
                for c in hmp[node]:
                    dp[node] += dfs(c, hmp, dp)

                return dp[node]

        dp = {}
        for t in tree:
            dfs(t.val, hmp, dp)  # find all the children, and see if the count is matching with total nodes in the tree
            # print(dp)
            if dp[t.val] == len(tree):
                return t




