# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(output, node,v):
            if node.val == v:
                output.append(node)
            else:
                if v < node.val:
                    if node.left:
                        dfs(output, node.left, v)
                elif v > node.val:
                    if node.right:
                        dfs(output, node.right, v)
        output = []
        if root == None: return None
        else:
            dfs(output, root, val)
            return output[0] if output != [] else None