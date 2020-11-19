# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        def flat(hmp, node, lvl):
            if node.left == node.right == None:
                hmp[node.val] = lvl
            else:
                hmp[node.val] = lvl
                if node.left:
                    flat(hmp, node.left, lvl + 1)
                if node.right:
                    flat(hmp, node.right, lvl + 1)

        hmp = {}
        flat(hmp, root, 0)

        # print(hmp)
        def trim(hmp, node, lvl):
            if node.left:
                if node.left.right:
                    if hmp[node.left.right.val] == lvl + 1:
                        node.left = None
                        return "Done"
                trim(hmp, node.left, lvl + 1)
            if node.right:
                if node.right.right:
                    if hmp[node.right.right.val] == lvl + 1:
                        node.right = None
                        return "Done"
                trim(hmp, node.right, lvl + 1)

        trim(hmp, root, 0)
        return root


