# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: 'Optional[TreeNode]') -> int: #BFS to find the first node with left, but without right
        if root == None:
            return 0 
        else:
            curr = 0
            stk = [root]
            while stk:
                nxt = []
                curr+= len(stk)
                while stk:
                    node = stk.pop(0)
                    if node.left and node.right:
                        nxt.append(node.left)
                        nxt.append(node.right)
                    elif node.left: #this is the first node in the layer without a right node, no need to check further
                        return curr + len(nxt) + 1 # nodes up to current layer + nxt + node.left
                        
                    elif node.left == node.right == None: 
                        return curr + len(nxt)
                stk = nxt 


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

