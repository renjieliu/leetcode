# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if p==q: return 0
        def find(path, curr, node, x):
            if node.val == x:
                path.append(curr+[node.val])
            else:
                if node.left:
                    find(path, curr+[node.val],  node.left, x)
                if node.right:
                    find(path, curr+[node.val], node.right,x)
        path = []
        find(path, [], root, p)
        find(path, [], root, q)
        a = path[0]
        b = path[1]
        while a and b and a[0] == b[0]: #prune the common roots, the rest is the distance
            a.pop(0)
            b.pop(0)
        return len(a) + len(b)
