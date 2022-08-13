# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: 'Optional[TreeNode]') -> bool: # O( N | 1 )
        def helper(node, L, R): #to check if current node is in the range (L, R)
            if node: # check if current node is within the range, and verify leftSubtree and rightSubtree
                return L < node.val < R and helper(node.left, L, node.val) and helper(node.right, node.val, R)
            return True
        
        return helper(root,-float('inf'), float('inf'))

    


# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: 'Optional[TreeNode]') -> bool: # O( N | 1 )
#         def helper(node, L, R): #to check if current node is in the range (L, R)
#             if node: # check if current node is within the range, and verify leftSubtree and rightSubtree
#                 return L < node.val < R and helper(node.left, L, node.val) and helper(node.right, node.val, R)
#             return True
        
#         return helper(root.left, -float('inf'), root.val) and helper(root.right, root.val, float('inf'))



# previous solution 

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(node, s, e):  # subTree 1: left, 2: right. s: ValidRangeStart, e:ValidRangeEnd
#             if node.left == node.right == None:
#                 return True
#             else:
#                 left = right = True
#                 if node.left:
#                     if node.left.val < node.val and s < node.left.val < e:
#                         left = helper(node.left, s, node.val)
#                     else:
#                         left = False

#                 if node.right:
#                     if node.right.val > node.val and s < node.right.val < e:
#                         right = helper(node.right, node.val, e)
#                     else:
#                         right = False

#                 return left & right

#         return helper(root, -float('inf'), float('inf'))






# previous approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def validate(node, left, right):  # node, leftboundary and rightboundary
#             if node.left == node.right == None:
#                 return True if left < node.val < right else False
#             else:
#                 if node.left:
#                     if left < node.left.val < node.val:
#                         if validate(node.left, left, node.val) == False: return False
#                     else:
#                         return False
#                 if node.right:
#                     if node.val < node.right.val < right:
#                         if validate(node.right, node.val, right) == False: return False
#                     else:
#                         return False
#                 return True
#
#         if root == None:
#             return True
#         else:
#             return validate(root, -float('inf'), float('inf'))



