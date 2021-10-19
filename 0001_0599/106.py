# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> TreeNode:
        hmp = {}
        for i, v in enumerate(inorder):  # the location in the tree
            hmp[v] = i

        def helper(in_left, in_right, postorder, hmp):
            if in_left <= in_right:
                root = TreeNode(postorder.pop())  # use the last item as the curr root
                currPos = hmp[root.val]  # curr position, split the inorder to left and right trees
                root.right = helper(currPos + 1, in_right, postorder, hmp)
                root.left = helper(in_left, currPos - 1, postorder, hmp)
                return root

        return helper(0, len(postorder) - 1, postorder, hmp)


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