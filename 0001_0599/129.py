# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: 'Optional[TreeNode]') -> int:
        def helper(output, node):  
            if node.left == node.right == None: # if it's leaf, just add and return the power as 0
                output[0] += node.val 
                return [0]
            else:
                leftpower = []
                rightpower = []
                paths  = []
                if node.left: # if the node has more than 1 children, it needs to be for all the paths below
                    leftpower = helper(output, node.left)
                    for p in leftpower:
                        output[0] += (node.val * (10**(p+1)))
                        paths.append(p+1)
                if node.right:
                    rightpower = helper(output, node.right)
                    for p in rightpower:
                        output[0] += (node.val * (10**(p+1)))
                        paths.append(p+1)
                return paths
                
        output = [0]
        helper(output, root)
        return output[0]
            


# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def sumNumbers(self, root: TreeNode) -> int:
#         def helper(node, curr, flat) :
#             if node.left == node.right:
#                 flat.append( int(''.join(curr)+str(node.val)))
#             else:
#                 if node.left:helper(node.left, curr+[str(node.val)], flat)
#                 if node.right:helper(node.right, curr+[str(node.val)], flat)
#         if root == None: return 0
#         else:
#             flat = []
#             helper(root, [], flat)
#             return sum(flat)