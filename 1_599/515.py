# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> 'List[int]':
        def flat(node, level, hmp):
            if node.left == node.right == None:
                if level not in hmp:
                    hmp[level] = []
                hmp[level].append(node.val)
            else:
                if level not in hmp:
                    hmp[level] = []
                hmp[level].append(node.val)
                if node.left != None:
                    flat(node.left, level + 1, hmp)
                if node.right != None:
                    flat(node.right, level + 1, hmp)

        if root == None: return []
        hmp = {}
        flat(root, 0, hmp)
        output = []
        for k in sorted(hmp.keys()):  # from level 0 to last level, for each level, add the max to the output
            output.append(max(hmp[k]))
        return output