# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        if root == None:
            return None
        def helper(output, node, prev):
            if node.left == node.right == None:
                output[0] = node
            else:
                helper(output, node.left, node)
            if prev: # just reconnect the left node, and cut off the pointer of the prev node
                node.left = prev.right
                node.right = prev
                prev.left = None
                prev.right = None

        output = [None]
        helper(output, root, None)
        return output[0]
