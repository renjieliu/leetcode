# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: 'Optional[TreeNode]') -> 'List[int]': # O( N | N )
        stk = []
        output = []
        curr = root 
        while curr or stk: #keep reading from the stk.
            while curr: # keep reading the left node
                stk.append(curr)
                curr = curr.left 
            curr = stk.pop() # add current node to the output
            output.append(curr.val)
            curr = curr.right # shift to the right node
        
        return output



# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def inorderTraversal(self, root: 'Optional[TreeNode]') -> 'List[int]': # O( N | 1 )
#         if root:
#             return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) # left, curr, right
#         return []
        


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> 'List[int]':
#         def flat(output, node):
#             if node.left == node.right ==None:
#                 output.append(node.val)
#             else:
#                 if node.left != None:
#                     flat(output, node.left)
#                 output.append(node.val)
#                 if node.right !=None:
#                     flat(output, node.right)

#         output = []
#         if root == None: return output
#         else:
#             flat(output, root)
#         return output


