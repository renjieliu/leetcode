# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: 'Optional[TreeNode]') -> int: # O( N | 1 )
        def helper(output, node): 
            if node.left == node.right == None:
                output[0] = max(output[0], 1)
                return [0, 0] #[decreasing, increasing]
            else:
                curr = 1
                L = [0, 0] #[decreasing, increasing]
                R = [0, 0] #[decreasing, increasing]
                if node.left:
                    if node.left.val == node.val-1:
                        L[0] = 1 + helper(output, node.left)[0] #add the decreasing sequence from left child
                    elif node.left.val == node.val + 1: 
                        L[1] = 1 + helper(output, node.left)[1] #add the increasing sequence from left child
                    else:
                        helper(output, node.left)
                
                if node.right:
                    if node.right.val == node.val-1:
                        R[0] = 1 + helper(output, node.right)[0] #add the decreasing sequence from right child
                    elif node.right.val == node.val + 1: 
                        R[1] = 1 + helper(output, node.right)[1] #add the increasing sequence from right child
                    else:
                        helper(output, node.right)
                
                output[0] = max(output[0], 1+L[0] + R[1], 1+L[1]+R[0])
                return [max(L[0], R[0]), max(L[1], R[1])] #max decreasing from left or right, max increasing from left or right
        
        output = [0]
        helper(output, root)
        return output[0]
        
 

# previous solution 

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def longestConsecutive(self, root: TreeNode) -> int:
#         def helper(output, node):
#             if node.left == node.right == None:
#                 return [1,1] #increase, decrease

#             A = B = 1 # increase, decrease
#             if node.left:
#                 leftLength = helper(output, node.left)
#                 if node.val == node.left.val + 1: # increase
#                     A = leftLength[0] + 1

#                 elif node.val == node.left.val - 1: # decrease
#                     B = leftLength[1] + 1

#             if node.right:
#                 rightLength = helper(output, node.right)
#                 if node.val == node.right.val + 1: # increase
#                     A = max(A, rightLength[0] + 1)

#                 elif node.val == node.right.val - 1: # decrease
#                     B = max(B, rightLength[1] + 1)

#             output[0] = max(output[0], A+B-1) # left + right - curr, as curr has been added twice
#             return [A,B]

#         output = [1] #current node. so the output is at least 1
#         helper(output, root)
#         return output[0]




# previous approach, copied the solution
# # Definition for a binary tree node.
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def longestConsecutive(self, root: TreeNode) -> int:
#         def longest_path(root: TreeNode):
#             nonlocal maxval
#
#             if not root:
#                 return [0, 0]
#
#             inr = dcr = 1
#             if root.left:
#                 left = longest_path(root.left)
#                 if (root.val == root.left.val + 1):
#                     dcr = left[1] + 1
#                 elif (root.val == root.left.val - 1):
#                     inr = left[0] + 1
#
#             if root.right:
#                 right = longest_path(root.right)
#                 if (root.val == root.right.val + 1):
#                     dcr = max(dcr, right[1] + 1)
#                 elif (root.val == root.right.val - 1):
#                     inr = max(inr, right[0] + 1)
#
#             maxval = max(maxval, dcr + inr - 1)
#             return [inr, dcr]
#
#         maxval = 0
#         longest_path(root)
#         return maxval
#
#
#
