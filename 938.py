# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(output, node):
            if node == None: return None
            if L<=node.val<=R:
                output.append(node.val)
                if node.left!= None:
                    dfs(output, node.left)
                if node.right!=None:
                    dfs(output, node.right)
            elif node.val>R and node.left!=None:
                dfs(output, node.left)
            elif node.val<L and node.right!=None:
                dfs(output, node.right)

        output = [0]
        dfs(output, root)
        return sum(output)