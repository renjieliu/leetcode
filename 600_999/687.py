# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def helper(node, output):
            if node.left == node.right == None:
                return 0
            else:
                left = right = 0
                if node.left:
                    if node.left.val == node.val:
                        left += 1 + helper(node.left, output)  # using current left as the node, and go down
                    else:
                        helper(node.left, output)
                if node.right:
                    if node.right.val == node.val:
                        right += 1 + helper(node.right, output)  # using current right as the node, and go down
                    else:
                        helper(node.right, output)

                output[0] = max(output[0], left + right)
                return max(left, right)

        if root == None: return 0
        output = [0]
        helper(root, output)
        return output[0]

