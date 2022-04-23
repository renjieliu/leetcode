# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: 'Optional[TreeNode]') -> None: #O(N | N)
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(node, idx): #flat the tree to an array
            return (flat(node.left, 2*idx+1) + [[node.val, idx]] + flat(node.right, 2*idx+2)) if node else []
        
        def findSwap(arr): #to find the last node, with the smallest value can be swapped with the first swappable node
            idx1 = [-1, -1]
            idx2 = [-1, -1]
            for i in range(len(arr)-1):
                if arr[i][0] > arr[i+1][0]: #keep updating, until find the last smallest ode
                    idx1 = arr[i+1]
                    if idx2 == [-1, -1]: #fix the first node
                        idx2 = arr[i]
                        
            return [idx1, idx2]
        
        def recover(node, idx, idx1, idx2): #swap the value in the tree
            if node:
                if idx == idx1[1]:
                    node.val = idx2[0]
                elif idx == idx2[1]:
                    node.val = idx1[0]
                recover(node.left, idx*2+1, idx1, idx2)
                recover(node.right, idx*2+2, idx1, idx2)
        
        arr = flat(root, 0)
        idx1, idx2 = findSwap(arr)
        recover(root, 0, idx1, idx2)
        
        


# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def recoverTree(self, root: 'Optional[TreeNode]') -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def flat(node, idx): #flat the tree to an array
#             return (flat(node.left, 2*idx+1) + [[node.val, idx]] + flat(node.right, 2*idx+2)) if node else []
        
#         def findSwap(arr): #to find the last node, with the smallest value can be swapped with the first swappable node
#             idx1 = [-1, -1]
#             idx2 = [-1, -1]
#             for i in range(len(arr)-1):
#                 if arr[i][0] > arr[i+1][0]: #keep updating, until find the last smallest ode
#                     idx1 = arr[i+1]
#                     if idx2 == [-1, -1]: #fix the first node
#                         idx2 = arr[i]
                        
#             return [idx1, idx2]
        
#         def recover(node, idx, idx1, idx2): #swap the value in the tree
#             if node:
#                 if idx == idx1[1]:
#                     node.val = idx2[0]
#                 elif idx == idx2[1]:
#                     node.val = idx1[0]
#                 recover(node.left, idx*2+1, idx1, idx2)
#                 recover(node.right, idx*2+2, idx1, idx2)
        
#         arr = flat(root, 0)
#         idx1, idx2 = findSwap(arr)
#         recover(root, 0, idx1, idx2)
        
       


# previous solution

# class Solution:
#     def recoverTree(self, root: 'TreeNode'):
#         """
#         :rtype: void Do not return anything, modify root in-place instead.
#         """

#         def inorder(r: TreeNode) -> List[int]:
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []

#         def find_two_swapped(nums: List[int]) -> (int, int):
#             n = len(nums)
#             x = y = -1
#             for i in range(n - 1):
#                 if nums[i + 1] < nums[i]:
#                     y = nums[i + 1]
#                     # first swap occurence
#                     if x == -1:
#                         x = nums[i]
#                     # second swap occurence
#                     else:
#                         break
#             return x, y

#         def recover(r: TreeNode, count: int):
#             if r:
#                 if r.val == x or r.val == y:
#                     r.val = y if r.val == x else x
#                     count -= 1
#                     if count == 0:
#                         return
#                 recover(r.left, count)
#                 recover(r.right, count)

#         nums = inorder(root)
#         x, y = find_two_swapped(nums)
#         recover(root, 2)


