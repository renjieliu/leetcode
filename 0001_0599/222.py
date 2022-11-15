# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: 'Optional[TreeNode]') -> int: # O( hlogN | 1 ) , h is the height of the tree
        if root == None:
            return 0
        lvls = lambda node: (1 + lvls(node.left)) if node else 0 # total levels in the tree
        h = lvls(root) - 1 # -1 to make it easier for the last level nodes count. last level total count should be 2**(h-1)
        def exists(node, idx, h): # to find the last exists node index
            s = 0 
            e = 2**h-1
            for _ in range(h):
                mid = (s+e)//2
                if idx <= mid:
                    e = mid - 1
                    node = node.left
                else:
                    s = mid + 1 
                    node = node.right
            return node != None          
            
        s = 0 # start node index on the last row 
        e = 2**h-1 # end node index on the last row
        last = 0
        while s <= e: # binary search to find the first missed index on the last row
            mid = (s+e)//2 
            if exists(root, mid, h):
                last = mid+1 # count is index + 1
                s = mid + 1 
            else:
                e = mid -1 
        
        return 2**h-1 + last # last index +1 is the count of nodes in the tree
            

    



# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def countNodes(self, root: 'Optional[TreeNode]') -> int: # O( N | N )
#         return (self.countNodes(root.left) + 1 + self.countNodes(root.right)) if root else 0 



# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def countNodes(self, root: 'Optional[TreeNode]') -> int:
#         if root == None:
#             return 0 
#         else:
#             h = 0
#             node = root
#             while node.left:
#                 h+=1 
#                 node = node.left
#             if h == 0:
#                 return 1 
#             else:
#                 def exists(node, idx, h): #check if current idx is a not None node
#                     left = 0
#                     right = 2**h - 1
#                     for _ in range(h):
#                         mid = (left+ right) // 2
#                         if idx <= mid:
#                             node = node.left
#                             right = mid - 1 
#                         else:
#                             node = node.right
#                             left = mid + 1 
#                     return node != None
                    
                
#                 left = 0
#                 right = 2**h-1
#                 index = float('inf') # index of the last not None node in the last row
#                 while left <= right: # binary search to find the last not None node
#                     mid = (left+ right) // 2 
#                     if exists(root, mid, h):
#                         left = mid + 1
#                         index = mid
#                     else:
#                         right = mid - 1
                
#                 return 2**h-1 + (index+1) # index+1 is the count
                

                
                



# previous approach
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def countNodes(self, root: 'Optional[TreeNode]') -> int: #BFS to find the first node with left, but without right
#         if root == None:
#             return 0 
#         else:
#             curr = 0
#             stk = [root]
#             while stk:
#                 nxt = []
#                 curr+= len(stk)
#                 while stk:
#                     node = stk.pop(0)
#                     if node.left and node.right:
#                         nxt.append(node.left)
#                         nxt.append(node.right)
#                     elif node.left: #this is the first node in the layer without a right node, no need to check further
#                         return curr + len(nxt) + 1 # nodes up to current layer + nxt + node.left
                        
#                     elif node.left == node.right == None: 
#                         return curr + len(nxt)
#                 stk = nxt 


# previous approach 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         def flat(output, node):
#             if node.left == node.right == None:
#                 output.append(node.val)
#             else:
#                 output.append(node.val)
#                 if node.left:
#                     flat(output, node.left)
#                 if node.right:
#                     flat(output, node.right)

#         output = []
#         if root == None: return 0
#         flat(output, root)
#         return len(output)

