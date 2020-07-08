# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def flat(node, output, curr, target):
            if node.val == target:
                output.append(curr+[node])
            else:
                if node.left: flat(node.left, output, curr+[node], target)
                if node.right: flat(node.right, output, curr+[node], target)
        if root == None: return None 
        output = []
        flat(root, output, [], p.val) 
        flat(root, output, [], q.val) 
        while output[0] and output[1] and output[0][0] == output[1][0]:
            t = output[0].pop(0)
            output[1].pop(0)
        return t