# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def flat(output, node):
            if node.left == node.right == None:
                output.append(node.val)
            else:
                output.append(node.val)
                if node.left: flat(output, node.left)
                if node.right: flat(output, node.right)

        output = []
        flat(output, root)
        output.sort()
        hmp = {}
        for i, c in enumerate(output):
            hmp[c] = sum(output[i:])

        def change(hmp, node):
            if node.left == node.right == None:
                node.val = hmp[node.val]
            else:
                node.val = hmp[node.val]
                if node.left: change(hmp, node.left)
                if node.right: change(hmp, node.right)

        res = root
        change(hmp, res)
        return res