"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        def helper(root, curr, prev):
            nxt = curr.parent
            curr.parent = prev
            if curr.left == prev: curr.left = None  # if current left is the new parent
            if curr.right == prev: curr.right = None  # if current right is the new parent
            if curr == root:
                return curr
            if curr.left:
                curr.right = curr.left
            curr.left = helper(root, nxt, curr)

            return curr

        return helper(root, leaf, None)



