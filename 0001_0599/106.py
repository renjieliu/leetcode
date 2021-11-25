# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'Optional[TreeNode]':
        hmp = {c: i for i, c in enumerate(inorder)} # to record the position of each value in the inorder, which is split the tree to left, right
        def helper(hmp, postorder, s, e):
            if s <= e and postorder:
                root = TreeNode(postorder.pop()) #using current node as root and split the tree into 2 parts
                root.right = helper(hmp, postorder, hmp[root.val]+1, e) #build the right subtree first, as post order is reading right value first
                root.left = helper(hmp, postorder, s, hmp[root.val]-1)
                return root
        return helper(hmp, postorder, 0, len(postorder)-1)
    
    


# previous approach
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'Optional[TreeNode]':
#         loc = {}  # inorder is left, node, right. we can use this to find the loc of the node, and split the tree into 2 parts.
#         for i, c in enumerate(inorder):
#             loc[c] = i 
            
#         def helper(s, e, loc, postorder):
#             if s <= e:
#                 if postorder: #post order: left, right, root. now we need to build it backward, root, right, left
#                     root = TreeNode(postorder.pop()) # using current node as root, and split the tree
#                     split = loc[root.val]
#                     root.right = helper(split+1, e, loc, postorder) 
#                     root.left = helper(s,split-1, loc, postorder)
#                     return root
#         return helper(0, len(postorder)-1, loc, postorder)





# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # inorder = [9,3,15,20,7]
# # postorder = [9,15,7,20,3]
# class Solution:
#     def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> TreeNode:
#         hmp = {}
#         for i, v in enumerate(inorder):  # the location in the tree
#             hmp[v] = i

#         def helper(in_left, in_right, postorder, hmp):
#             if in_left <= in_right:
#                 root = TreeNode(postorder.pop())  # use the last item as the curr root
#                 currPos = hmp[root.val]  # curr position, split the inorder to left and right trees
#                 root.right = helper(currPos + 1, in_right, postorder, hmp)
#                 root.left = helper(in_left, currPos - 1, postorder, hmp)
#                 return root

#         return helper(0, len(postorder) - 1, postorder, hmp)


# previous apparoach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> TreeNode:
#         hmp = {}
#         for i, v in enumerate(inorder):
#             hmp[v] = i
#         def helper(in_left, in_right, postorder, hmp):
#             if in_left>in_right:
#                 return None
#             else:
#                 root = TreeNode(postorder.pop())
#                 currPos = hmp[root.val]
#                 root.right = helper(currPos +1,  in_right,  postorder, hmp)
#                 root.left = helper(in_left, currPos-1, postorder, hmp)
#                 return root
#         return helper(0, len(postorder)-1, postorder, hmp)