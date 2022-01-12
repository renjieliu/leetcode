# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: 'Optional[TreeNode]', val: int) -> 'Optional[TreeNode]':
        def helper(added, node, L, R, val): #L, R to store value range of the current node
            if added[0] == None:
                if node.left == None and L <= val < node.val:
                    node.left = TreeNode(val)
                    added[0] = 1 
                if node.right == None and node.val < val <= R:
                    node.right = TreeNode(val)
                    added[0] = 1 

                if node.left and added[0] == None:
                    helper(added, node.left, L, node.val, val)
                if node.right and added[0] == None:
                    helper(added, node.right, node.val, R, val)
        
        if root == None:
            return TreeNode(val)
        added = [None] # to flag if the node is added
        helper(added, root, -float('inf'), float('inf'), val)
        return root
    



    


# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         def dfs(output, node):
#             if node.left == node.right == None:
#                 output.append(node.val)
#             else:
#                 output.append(node.val)
#                 if node.left: dfs(output, node.left)
#                 if node.right: dfs(output, node.right)

#         if root == None:
#             return TreeNode(val)
#         else:
#             output = [val]
#             dfs(output, root)
#             output.sort()
#             start = TreeNode(output[0])
#             node = start
#             for o in output[1:]:
#                 node.right = TreeNode(o)
#                 node = node.right
#             return start
