# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None: return True

        def helper(output, node, level, ans):
            if node.left == node.right == None:  # return the level of current node
                output[0] = level
                ans.append(1)
            else:
                l = r = level
                if node.left:
                    helper(output, node.left, level + 1, ans)
                    l = output[0]
                if node.right:
                    helper(output, node.right, level + 1, ans)
                    r = output[0]

                output[0] = max(l, r)  # the max leaf layer

                ans.append(0 if abs(l - r) > 1 else 1)

        ans = []
        helper([0], root, 0, ans)
        return 0 not in ans