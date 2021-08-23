# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: #RL 20210823: #simple DFS approach O(n) + space O(n)
    def findTarget(self, root: 'Optional[TreeNode]', k: int) -> bool:
        def helper(lkp, node, k):
            if k-node.val in lkp :
                return True
            else:
                lkp.add(node.val)
                A = B = False
                if node.left:
                    A = helper(lkp, node.left, k)
                    if A:
                        return True
                if node.right:
                    B = helper(lkp, node.right, k)
                    if B:
                        return True
                return False
        lkp = set()
        return helper(lkp, root, k)


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution: #RL 20210823: O(n^2) + Space:O(1) approach
#     def findTarget(self, root: 'Optional[TreeNode]', k: int) -> bool:
#         def dfs(node, root, k): #check each node, and find if it can find a match in the tree
#             res = find(root, k-node.val, node.val)
#             if res:
#                 return True
#             else:
#                 if node.left:
#                     res = dfs(node.left, root, k)
#                     if res:
#                         return True
#                 if node.right:
#                     res = dfs(node.right, root, k)
#                     if res:
#                         return True
#             return False
#
#         def find(node, v, ori):
#             if node.val == v:
#                 return True if v!=ori else False
#             else:
#                 if v > node.val:
#                     return find(node.right, v, ori) if node.right else False
#                 if v < node.val:
#                     return find(node.left, v, ori) if node.left else False
#
#
#         return dfs(root, root, k)






# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution: #RL 20210823: O(nlogn) + Space:O(n) approach
#     def findTarget(self, root: 'Optional[TreeNode]', k: int) -> bool:
#         def dfs(arr, node):
#             arr.append(node.val)
#             if node.left:
#                 dfs(arr, node.left)
#             if node.right:
#                 dfs(arr, node.right)
#         def binFind(arr, v):
#             if arr == []: return False
#             if v<arr[0] or v>arr[-1]:
#                 return False
#             else:
#                 s = 0
#                 e = len(arr) -1
#                 while s <= e:
#                     mid = (s+e)//2
#                     if arr[mid] == v :
#                         return True
#                     else:
#                         if arr[mid] > v:
#                             e = mid -1
#                         else:
#                             s = mid + 1
#                 return False
#         arr = []
#         dfs(arr,root)
#         arr.sort()
#         for i, a in enumerate(arr):
#             if binFind(arr[i+1:], k-a) == True:
#                 return True
#         return False
#
#
#
#
#
#
#
#
#
#
#
#
