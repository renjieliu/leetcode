# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: 'List[int]') -> 'Optional[TreeNode]':
        def helper(node, leftRange, rightRange, arr):#[currentNode, leftChildRange, rightChildRange, preorder]
            if arr and leftRange[0] < arr[0] < leftRange[1]:
                node.left = TreeNode(arr.pop(0))
                helper(node.left, [leftRange[0], node.left.val], [node.left.val, node.val], arr)
            
            if arr and rightRange[0] < arr[0] < rightRange[1]:
                node.right = TreeNode(arr.pop(0))
                helper(node.right, [node.val, node.right.val], [node.right.val, rightRange[1]], arr)
        
        root = TreeNode(preorder.pop(0))
        helper(root, [-float('inf'), root.val], [root.val, float('inf')], preorder)
        return root



# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def bstFromPreorder(self, preorder: 'List[int]') -> TreeNode:
#         if preorder ==[]:return None
#         else:
#             root = TreeNode(preorder[0])
#             left = []
#             i = 1
#             while i < len(preorder) and preorder[i] < root.val:
#                 left.append(preorder[i])
#                 i+=1
#             right = preorder[i:]
#             root.left = self.bstFromPreorder(left)
#             root.right = self.bstFromPreorder(right)
#             return root


