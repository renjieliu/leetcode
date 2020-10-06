# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def flat(node, level, hmp):
            if level not in hmp:
                hmp[level] = []
            hmp[level].append(node.val)
            if node.left:
                flat(node.left, level + 1, hmp)
            if node.right:
                flat(node.right, level + 1, hmp)

        hmp = {}
        flat(root, 0, hmp)
        # print(hmp)
        for k, v in hmp.items():
            if v[0] % 2 == k % 2:
                return False
            for i in range(1, len(v)): #node val of even level should be odd and increasing, of odd level should be even and decreasing
                if v[i] % 2 == k % 2 or (k % 2 == 0 and v[i] <= v[i - 1]) or (k % 2 != 0 and v[i] >= v[i - 1]):
                    return False
        return True






