# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def mark(node, target):  # this is to mark all the nodes to be deleted
            if node.left == node.right == None:  # the leaf can be removed
                if node.val == target:
                    return 1  # 1: current node can be removed, 0: keep current node
                return 0
            else:
                a = b = -1
                if node.left:
                    a = mark(node.left, target)
                    if a == 1:
                        node.left = None
                if node.right:
                    b = mark(node.right, target)
                    if b == 1:
                        node.right = None

                if (a == b == 1) or (a == 1 and b == -1) or (a == -1 and b == 1):  # leaf can be removed
                    if node.val == target:
                        return 1
                    else:
                        return 0

        if mark(root, target) == 1:
            return None
        else:
            return root
