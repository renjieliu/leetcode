# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: 'Optional[TreeNode]') -> int:
        def dfs(output, node, flag): #flag = 0: root, 1: left, 2: right
            if node.left == node.right == None:
                if flag == 1:
                    output[0] += node.val
            else:
                if node.left:
                    dfs(output, node.left, 1)
                if node.right:
                    dfs(output, node.right, 2)
        
        output = [0]  
        dfs(output, root, 0) #dummy number for the root
        return output[0]
    


# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sumOfLeftLeaves(self, root: TreeNode) -> int:
#         def flat(node, output, direction):
#             if node.left == node.right == None:
#                 output[-1] += node.val if direction == 1 else 0
#             else:
#                 if node.left:
#                     flat(node.left, output, 1)
#                 if node.right:
#                     flat(node.right, output, 2)

#         if root == None:
#             return 0
#         else:
#             output = [0]
#             flat(root, output, 0)
#             return output[0]
