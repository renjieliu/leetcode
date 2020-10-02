# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findNearestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        hmp = {}  # to store all the level, and index
        target_Level_idx = [-1, -1]

        def flat(node, hmp, lvl, idx, v, target_Level):
            if node.val == v:
                target_Level_idx[0] = lvl
                target_Level_idx[1] = idx
            if lvl not in hmp:
                hmp[lvl] = []
            hmp[lvl].append([idx, node])
            if node.left == node.right == None:
                return None
            else:
                if node.left:
                    flat(node.left, hmp, lvl + 1, idx * 2 + 1, v, target_Level_idx)
                if node.right:
                    flat(node.right, hmp, lvl + 1, idx * 2 + 2, v, target_Level_idx)

        flat(root, hmp, 0, 0, u.val, target_Level_idx)
        if target_Level_idx[0] == -1:
            return None
        else:
            arr = hmp[target_Level_idx[0]]
            arr.sort(key=lambda x: x[0])
            for a in arr:  # on the same level, find the first one on the right of the node
                if a[0] > target_Level_idx[1]:
                    return a[1]
            return None























