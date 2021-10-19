# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def flat(path, curr, node):
            if node.left == node.right == None:
                path.append(curr + [node.val])
            else:
                if node.left: flat(path, curr + [node.val], node.left)
                if node.right: flat(path, curr + [node.val], node.right)

        path = []
        flat(path, [], root)
        maxLevel = max([len(p) for p in path])
        arr = [p for p in path if len(p) == maxLevel]
        target = arr[0][0]
        while arr[0]:
            curr = arr[0][0]
            lkp = set()
            for a in arr:
                lkp.add(a.pop(0))
            if len(lkp) == 1:
                target = curr
            else:
                break

        def findTarget(target, node, output):
            if node.val == target:
                output[0] = node
            else:
                if node.left: findTarget(target, node.left, output)
                if node.right: findTarget(target, node.right, output)

        output = [None]
        findTarget(target, root, output)
        return output[0]





















