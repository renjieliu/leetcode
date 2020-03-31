# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def flat(node, path):
            if node.left == node.right ==None:
                path.append(node.val)
            else:
                path.append(node.val)
                if node.left: flat(node.left, path)
                if node.right: flat(node.right, path)
        path = []
        flat(root, path)
        return sorted(path)[k-1]