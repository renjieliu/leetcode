# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def helper(output, node):
            if node.left == node.right == None:
                return [1,1] #increase, decrease

            A = B = 1 # increase, decrease
            if node.left:
                leftLength = helper(output, node.left)
                if node.val == node.left.val + 1: # increase
                    A = leftLength[0] + 1

                elif node.val == node.left.val - 1: # decrease
                    B = leftLength[1] + 1

            if node.right:
                rightLength = helper(output, node.right)
                if node.val == node.right.val + 1: # increase
                    A = max(A, rightLength[0] + 1)

                elif node.val == node.right.val - 1: # decrease
                    B = max(B, rightLength[1] + 1)

            output[0] = max(output[0], A+B-1) # left + right - curr, as curr has been added twice
            return [A,B]

        output = [1] #current node. so the output is at least 1
        helper(output, root)
        return output[0]




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
