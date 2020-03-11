# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node,output, depth, v):
            if node:
                if node.left==node.right ==None:
                    return 0
                elif (node.left!=None and node.left.val == v) or (node.right !=None and node.right.val == v):
                    output.append([node.val, depth, v]) #parent, level,  value
                    return 1
                else:
                    dfs(node.left, output, depth+1, v)
                    dfs(node.right,output, depth+1, v)
        output = []
        dfs(root, output, 0, x)
        dfs(root, output, 0, y)
        if len(output) !=2:
            return False
        return True if output[0][0] != output[1][0] and output[0][1] == output[1][1] else False