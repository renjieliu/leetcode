# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> 'List[int]':
        def dfs(output, node):
            if node.left == node.right == None:
                output.append(node.val)
            else:
                output.append(node.val)
                if node.left: dfs(output, node.left)
                if node.right: dfs(output, node.right)

        output = []
        for r in (root1, root2):
            if r: dfs(output, r)

        return sorted(list(output))