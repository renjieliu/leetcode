# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> 'List[int]':
        if root == None: return []
        output = []
        def find(node,output):
            if node:
                output.append(node.val)
                if node.left != None:
                    find(node.left, output)
                if node.right != None:
                    find(node.right, output)
        find(root, output)
        return output