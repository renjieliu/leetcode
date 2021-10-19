# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(t1, t2, output):
            if (t1 and t1.left == t1.right == None) and (t2 and t2.left == t2.right == None):
                return
            else:
                if (t1 and t1.left) or (t2 and t2.left):
                    curr = (0 if t1 == None or t1.left == None else t1.left.val) + (
                        0 if t2 == None or t2.left == None else t2.left.val)
                    output.left = TreeNode(curr)
                    dfs(t1.left if t1 and t1.left else None, t2.left if t2 and t2.left else None, output.left)

                if (t1 and t1.right) or (t2 and t2.right):
                    curr = (0 if t1 == None or t1.right == None else t1.right.val) + (
                        0 if t2 == None or t2.right == None else t2.right.val)
                    output.right = TreeNode(curr)
                    dfs(t1.right if t1 and t1.right else None, t2.right if t2 and t2.right else None, output.right)

        if t1 == t2 == None:
            return None

        else:
            output = TreeNode((0 if t1 == None else t1.val) + (0 if t2 == None else t2.val))
            dfs(t1, t2, output)
            return output



