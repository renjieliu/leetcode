# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        def helper(preorder, inorder,lkp):#find current node val pos in the inorder list. values on the left form left tree and values on the right form righ tree
            if len(inorder) == 0:
                return None
            elif len(inorder) == 1:
                lkp.add(inorder[0])
                return TreeNode(inorder.pop(0))
            else:
                node = None
                while preorder and preorder[0] in lkp:
                    preorder.pop(0)
                if preorder:
                    node = TreeNode(preorder.pop(0))
                    idx = inorder.index(node.val)
                    node.left = helper(preorder,inorder[:idx], lkp)
                    node.right = helper(preorder,inorder[idx+1:], lkp)
                return node
        return helper(preorder, inorder, set())
