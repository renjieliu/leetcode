# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: 'Optional[TreeNode]') -> 'List[int]': # O( N | 1 )
        output = [] 
        curr = root
        while curr: #Morris Traversal, make all the current as the the right of the rightmost of the left tree - this is what the in-order traversa looks like
            if curr.left == None:
                output.append(curr.val)
                curr = curr.right
            else: 
                r = curr.left
                while r.right: # make curr as the right node of the rightmost node in the left sub tree
                    r = r.right 
                r.right = curr
                t = curr
                curr = curr.left # move curr to curr left, and make 
                t.left = None # cut off the previous root left
        
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
#         output = [] 
#         curr = root
#         while curr:
#             if curr.left == None:
#                 output.append(curr.val)
#                 curr = curr.right
#             else: 
#                 r = curr.left
#                 while r.right:
#                     r = r.right 
#                 r.right = curr
#                 t = curr
#                 curr = curr.left 
#                 t.left = None
        
#         return output
    


# previous solution 

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def inorderTraversal(self, root: 'Optional[TreeNode]') -> 'List[int]': # O( N | 1 )
#         output = []
#         curr = root
#         while curr:  #Morris Traversal, make all the current as the the right of the rightmost of the left tree - this is what the in-order traversa looks like
#             if curr.left == None:
#                 output.append(curr.val)
#                 curr = curr.right
#             else:
#                 prev = curr.left # in the left tree, make curr as the right child of the rightmost node
#                 while prev.right:
#                     prev = prev.right
#                 prev.right = curr 
#                 t = curr 
#                 curr = curr.left # check the next left child 
#                 t.left = None # cut off the previous left node
#         return output
    

    





# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def inorderTraversal(self, root: 'Optional[TreeNode]') -> 'List[int]': # O( N | N )
#         stk = []
#         output = []
#         curr = root 
#         while curr or stk: #keep reading from the stk.
#             while curr: # keep reading the left node
#                 stk.append(curr)
#                 curr = curr.left 
#             curr = stk.pop() # add current node to the output
#             output.append(curr.val)
#             curr = curr.right # shift to the right node
        
#         return output



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


