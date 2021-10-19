# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def flat(path, node, target, curr):
            if node.val == target:
                path.append(curr + [node.val])
                return
            else:
                if node.left:
                    flat(path, node.left, target, curr + [node.val])
                if node.right:
                    flat(path, node.right, target, curr + [node.val])

        def findNode(output, node, target):  # find the node
            if node.val == target:
                output.append(node)
            else:
                if node.left:
                    findNode(output, node.left, target)
                if node.right:
                    findNode(output, node.right, target)

        path = []
        flat(path, root, p.val, [])
        flat(path, root, q.val, [])
        # print(path)
        if len(path) < 2:
            return None
        else:
            while path[0] and path[1]:
                a = path[0].pop(0)
                b = path[1].pop(0)
                if a == b:
                    x = a
            # x = list(set(path[0]) & (set(path[1])))  #to find the LCA value
            output = []
            findNode(output, root, x)  # use the value to find the node and return
            return output[0]





















