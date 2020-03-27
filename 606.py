# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(output, node):
            if node.left == None and node.right == None:
                output.append(str(node.val))
            else:
                output.append(str(node.val))
                if node.left != None:
                    output.append("(")
                    dfs(output, node.left)
                    output.append(")")
                else:
                    output.append("()")

                if node.right != None:
                    output.append("(")
                    dfs(output, node.right)
                    output.append(")")

        if t == None: return ""
        output = []
        dfs(output, t)
        return "".join(output)

