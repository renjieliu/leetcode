# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> 'List[List[int]]':
        def flat(output, curr, path, node, target):
            if node.left == node.right == None:
                if node.val+curr == target:
                    output.append(path + [node.val])
            else:
                if node.left:
                    flat(output, curr+node.val, path + [node.val], node.left, target)
                if node.right:
                    flat(output, curr+node.val, path + [node.val], node.right, target)
        if root == None: return []
        else:
            output = []
            flat(output, 0, [], root, sum)
            return output