# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> 'List[float]':
        def dfs(hmp, node, level):
            if level not in hmp:
                hmp[level] = []
            hmp[level].append(node.val)
            if node.left:
                dfs(hmp, node.left, level+1)
            if node.right:
                dfs(hmp, node.right, level+1)
        if root == None:
            return []
        hmp = {}
        dfs(hmp, root, 0)
        for k, v in hmp.items():
            hmp[k] = sum(v)/len(v)
        return [hmp[k] for k in sorted(hmp.keys())]