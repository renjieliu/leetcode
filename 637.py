# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> 'List[float]':
        def flat(output, node, level):
            if level >= len(output):
                output.append([])
            if node.left == node.right == None:
                output[level - 1].append(node.val)
            else:
                output[level - 1].append(node.val)
                if node.left:
                    flat(output, node.left, level + 1)
                if node.right:
                    flat(output, node.right, level + 1)

        if root == None:
            return []
        else:
            output = []
            flat(output, root, 1)
            res = [sum(o) / len(o) for o in output if o]
            return res

