# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(level, hmp, node):
            if node.left == node.right == None:
                if level not in hmp:
                    hmp[level] = []
                hmp[level].append(node.val)
            else:
                if level not in hmp:
                    hmp[level] = []
                hmp[level].append(node.val)
                if node.left != None:
                    dfs(level + 1, hmp, node.left)
                if node.right != None:
                    dfs(level + 1, hmp, node.right)

        hmp = {}
        dfs(1, hmp, root)
        return sorted(hmp.keys(), key=lambda x: sum(hmp[x]), reverse=True)[0]

