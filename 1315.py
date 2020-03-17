# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, output):
            curr = 0
            if node.left != None:
                if node.left.left != None and node.val % 2 == 0:
                    curr += node.left.left.val
                if node.left.right != None and node.val % 2 == 0:
                    curr += node.left.right.val
                if node.left.left != None or node.left.right != None:
                    dfs(node.left, output)

            if node.right != None:
                if node.right.left != None and node.val % 2 == 0:
                    curr += node.right.left.val
                if node.right.right != None and node.val % 2 == 0:
                    curr += node.right.right.val
                if node.right.left != None or node.right.right != None:
                    dfs(node.right, output)

            if curr != 0:
                output.append(curr)

        output = []
        if root == None:
            return 0
        else:
            dfs(root, output)
            return sum(output)

