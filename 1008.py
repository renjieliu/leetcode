# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: 'List[int]') -> TreeNode:
        if preorder ==[]:return None
        else:
            root = TreeNode(preorder[0])
            left = []
            i = 1
            while i < len(preorder) and preorder[i] < root.val:
                left.append(preorder[i])
                i+=1
            right = preorder[i:]
            root.left = self.bstFromPreorder(left)
            root.right = self.bstFromPreorder(right)
            return root