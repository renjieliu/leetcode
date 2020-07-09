# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def flat(output, curr, node, target):
            if node.val == target:
                output.append(curr + [node])
            else:
                if node.left:
                    flat(output, curr + [node], node.left, target)
                if node.right:
                    flat(output, curr + [node], node.right, target)

        if root == None: return None
        output = []  # there will be 2 paths in the output, 1 for p, 1 for q.
        flat(output, [], root, p.val)
        flat(output, [], root, q.val)
        while output[0] and output[1] and output[0][0] == output[1][0]:  # find the last common predecessor
            t = output[0].pop(0)
            output[1].pop(0)
        return t
