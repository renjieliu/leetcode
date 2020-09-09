# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flat(node, output):
            if node.left == node.right == None:
                output.append(node.val)
            else:
                output.append(node.val)
                if node.left:
                    flat(node.left, output)
                if node.right:
                    flat(node.right, output)

        if root:
            output = []
            flat(root, output)
            root.val = output[0]
            root.left = None
            node = root
            output.pop(0)
            while output:
                node.right = TreeNode(output.pop(0))
                node = node.right


