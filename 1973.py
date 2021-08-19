# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def equalToDescendants(self, root: 'Optional[TreeNode]') -> int:
        def helper(output, node):
            if node.left == node.right==None:
                output[0] += 1 if node.val == 0 else 0
                return node.val
            else:
                left = right = 0
                if node.left: #find the sum of left subtree
                    left = helper(output, node.left)
                if node.right: #find the sum of right subtree
                    right = helper(output, node.right)

                output[0] += 1 if node.val == left + right else 0
                return node.val + left + right #return the sum of the entire current tree
        output = [0]
        helper(output, root)
        return output[0]


