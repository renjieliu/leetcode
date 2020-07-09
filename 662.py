# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def flat(node, idx, level, hmp):
            if node.left == node.right == None:
                if level not in hmp:
                    hmp[level] = []
                hmp[level].append(idx)
            else:
                if level not in hmp:
                    hmp[level] = []
                hmp[level].append(idx)
                if node.left: flat(node.left, 2*idx+1, level +1 , hmp )
                if node.right: flat(node.right, 2*idx+2, level +1 , hmp )
        if root == None:
            return 0
        else:
            hmp ={}
            flat(root, 0, 0, hmp)
            output = -float('inf')
            for k, v in hmp.items():
                output = max(output,v[-1] - v[0] +1)
            return output