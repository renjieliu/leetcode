# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def nxt(flat, node):
            if node.left == node.right == None:
                flat.append(node.val)
            else:
                flat.append(node.val)
                if node.left:
                    nxt(flat, node.left)
                if node.right:
                    nxt(flat, node.right)

        if root == None: return None
        flat = []
        nxt(flat, root)
        s = sorted(list(set(flat)))
        hmp = {}
        for i in range(len(s)):
            if s[i] not in hmp:
                hmp[s[i]] = sum(s[i:])

        def compute(hmp, node):
            node.val = hmp[node.val]
            if node.left:
                compute(hmp, node.left)
            if node.right:
                compute(hmp, node.right)

        compute(hmp, root)
        return root
