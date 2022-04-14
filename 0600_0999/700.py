# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: 'Optional[TreeNode]', val: int) -> 'Optional[TreeNode]':#O(logN)
        if root:
            if root.val == val:
                return root
            elif val < root.val: # check the left sub-tree
                return self.searchBST(root.left, val)
            else: # check the right sub-tree
                return self.searchBST(root.right, val)
        return None
    
                


# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def searchBST(self, root: 'TreeNode', val: int) -> 'TreeNode':
#         def find(node, val, output):
#             if node.left == node.right == None:
#                 if node.val == val:
#                     output.append(node)
#             else:
#                 if node.val == val:
#                     output.append(node)
#                     return 
#                 else:
#                     if node.left:find(node.left, val, output)
#                     if node.right:find(node.right, val, output)
#         if root == None: return None 
#         output = []
#         find(root, val , output)
#         return None if output == [] else output[0]



# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         def dfs(output, node,v):
#             if node.val == v:
#                 output.append(node)
#             else:
#                 if v < node.val:
#                     if node.left:
#                         dfs(output, node.left, v)
#                 elif v > node.val:
#                     if node.right:
#                         dfs(output, node.right, v)
#         output = []
#         if root == None: return None
#         else:
#             dfs(output, root, val)
#             return output[0] if output != [] else None



