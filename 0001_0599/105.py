# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'Optional[TreeNode]': # O( N**2 | N )
        if inorder: # inorder can be used to split the tree into two 
            node = TreeNode(preorder.pop(0)) # since this has been popped, it will not be used again.
            idx = inorder.index(node.val)
            node.left = self.buildTree(preorder, inorder[:idx]) #the same number should not be used again
            node.right = self.buildTree(preorder, inorder[idx+1:])
            return node
    




# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'Optional[TreeNode]':  # O( N**2 | N )
#         def build(lkp, preorder, inorder):
#             if len(inorder) == 0:
#                 return None 
#             elif len(inorder) == 1:
#                 lkp.add(inorder[0])
#                 return TreeNode(inorder[0])
#             else:
#                 while preorder and preorder[0] in lkp: # find the node in the preorder, that's not seen before, and this is the new root.
#                     preorder.pop(0)
#                 curr = preorder.pop(0)
#                 lkp.add(curr)
#                 loc = inorder.index(curr) # find current number in the in order tree, and it can split the tree into two
#                 node = TreeNode(curr)
#                 node.left = build(lkp, preorder, inorder[:loc]) #left half 
#                 node.right = build(lkp, preorder, inorder[loc+1:]) #right half
#                 return node
#         return build(set(), preorder, inorder)
    
    

# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
#         def helper(preorder, inorder,lkp):#find current node val pos in the inorder list. values on the left form left tree and values on the right form righ tree
#             if len(inorder) == 0:
#                 return None
#             elif len(inorder) == 1:
#                 lkp.add(inorder[0])
#                 return TreeNode(inorder.pop(0))
#             else:
#                 node = None
#                 while preorder and preorder[0] in lkp:
#                     preorder.pop(0)
#                 if preorder:
#                     node = TreeNode(preorder.pop(0))
#                     idx = inorder.index(node.val)
#                     node.left = helper(preorder,inorder[:idx], lkp)
#                     node.right = helper(preorder,inorder[idx+1:], lkp)
#                 return node
#         return helper(preorder, inorder, set())
