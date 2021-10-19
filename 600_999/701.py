# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(output, node):
            if node.left == node.right == None:
                output.append(node.val)
            else:
                output.append(node.val)
                if node.left: dfs(output, node.left)
                if node.right: dfs(output, node.right)

        if root == None:
            return TreeNode(val)
        else:
            output = [val]
            dfs(output, root)
            output.sort()
            start = TreeNode(output[0])
            node = start
            for o in output[1:]:
                node.right = TreeNode(o)
                node = node.right
            return start
