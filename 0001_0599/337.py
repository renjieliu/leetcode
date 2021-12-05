# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: 'Optional[TreeNode]') -> int:
        def helper(hmp, idx, node): # using hmp to speed up the traversal
            if idx in hmp:
                return hmp[idx]
            hmp[idx] = 0
            if node == None: 
                hmp[idx] = 0
                return 0 
            if node.left == node.right == None:
                hmp[idx] = node.val
                return  hmp[idx]
            else:
                hmp[idx] = 0
                A = node.val # taken current val
                B = 0 # not taken
                if node.left:
                    A += helper(hmp, 2*(2*idx+1)+1, node.left.left)
                    A += helper(hmp, 2*(2*idx+1)+2, node.left.right)
                    B += helper(hmp, 2*idx+1, node.left)
                if node.right:
                    A += helper(hmp, 2*(2*idx+2)+1, node.right.left)
                    A += helper(hmp, 2*(2*idx+2)+2, node.right.right)
                    B += helper(hmp, 2*idx+2, node.right)
                hmp[idx] = max(A, B)
                return hmp[idx]
        
        return helper({}, 0, root)  
        

# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         def helper(node):
#             if node == None:
#                 return [0, 0]  # [robbed, notRobbed]
#             else:
#                 left = helper(node.left)
#                 right = helper(node.right)
#                 rob = node.val + left[1] + right[1]
#                 not_rob = max(left) + max(right)
#                 return [rob, not_rob]

#         return max(helper(root))

