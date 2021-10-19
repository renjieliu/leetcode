# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if node == None:
                return [0, 0]  # [robbed, notRobbed]
            else:
                left = helper(node.left)
                right = helper(node.right)
                rob = node.val + left[1] + right[1]
                not_rob = max(left) + max(right)
                return [rob, not_rob]

        return max(helper(root))

