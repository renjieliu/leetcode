# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: 'Optional[TreeNode]') -> str: # O( N | N )
        def helper(output, node):
            output[0] += str(node.val) if node else ""
            if node.left and node.right: #if both subtree exist
                output[0] += "(" 
                helper(output, node.left) 
                output[0] += ")"
                output[0] += "(" 
                helper(output, node.right) 
                output[0] += ")"
            elif node.left == None and node.right: #only right subtree exists
                output[0] += "()"
                output[0] += "(" 
                helper(output, node.right) 
                output[0] += ")"
            elif node.left and node.right == None: #only left subtree exists
                output[0] += "(" 
                helper(output, node.left) 
                output[0] += ")"
        output = [""]
        helper(output, root)
        return output[0]
            
        


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def tree2str(self, t: TreeNode) -> str:
#         def dfs(output, node):
#             if node.left == None and node.right == None:
#                 output.append(str(node.val))
#             else:
#                 output.append(str(node.val))
#                 if node.left != None:
#                     output.append("(")
#                     dfs(output, node.left)
#                     output.append(")")
#                 else:
#                     output.append("()")

#                 if node.right != None:
#                     output.append("(")
#                     dfs(output, node.right)
#                     output.append(")")

#         if t == None: return ""
#         output = []
#         dfs(output, t)
#         return "".join(output)

