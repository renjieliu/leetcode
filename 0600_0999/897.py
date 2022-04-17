# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.newRoot = TreeNode() #dummy new root, will return the first child node
        self.newNode = self.newRoot 
        
    def increasingBST(self, root: TreeNode) -> TreeNode: #O(N | N)
        if root.left == root.right == None:
            self.newNode.right = TreeNode(root.val) 
            self.newNode = self.newNode.right
        else: # in order traversal, from left to right, add current node to the newRoot.
            if root.left:
                self.increasingBST(root.left)
            self.newNode.right = TreeNode(root.val)  
            self.newNode = self.newNode.right
            if root.right:
                self.increasingBST(root.right)
            # print(self.newRoot)
        return self.newRoot.right




# previous solution

# # Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#         def flat(arr, node):
#             if node.left == node.right == None:
#                 arr.append(node.val)
#             else:
#                 if node.left:
#                     flat(arr, node.left)
#                     arr.append(node.val)
#                 if node.right:
#                     if node.left == None:  # if the node does not have left child, current node value needs to be pushed to the stack
#                         arr.append(node.val)
#                     flat(arr, node.right)

#         if root == None: return None
#         arr = []
#         flat(arr, root)
#         start = TreeNode(arr[0])
#         node = start
#         for a in arr[1:]:
#             node.right = TreeNode(a)
#             node = node.right
#         return start




