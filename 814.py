# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(node): #to get the sum of current node and children
            if node.left == node.right == None:
                return node.val
            l = r = 0
            if node.left:
                l += helper(node.left)
                if l == 0:
                    node.left = None
            if node.right:
                r += helper(node.right)
                if r == 0:
                    node.right = None

            return node.val+l+r

        p = TreeNode(-1) #make root as left of a dummy tree, if all the nodes are 0, root needs to be removed too
        p.left = root
        helper(p)

        return p.left

