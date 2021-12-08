# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: 'Optional[TreeNode]') -> int:
        def helper(output, node):
            if node == None:
                return 0 
            else:
                A = helper(output, node.left) #sum of left tree
                B = helper(output, node.right) # sum of right tree
                output[0] += abs(A-B) #add current tilt to the output
                return node.val + A + B # return total of current node
        output = [0]
        helper(output, root)

        return output[0]
    

# previous approach 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findTilt(self, root: TreeNode) -> int:
#         if root == None: return 0

#         def sumChildren(output, node):
#             if node.left == node.right == None:
#                 output.append(0)
#                 return node.val
#             l = r = 0
#             if node.left:
#                 l = sumChildren(output, node.left)
#             if node.right:
#                 r = sumChildren(output, node.right)
#             output.append(abs(l - r))
#             return l + r + node.val

#         output = []
#         sumChildren(output, root)
#         # print(output)
#         return sum(output)
