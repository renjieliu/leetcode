# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: 'Optional[TreeNode]') -> 'List[float]': # O( N | N )
        def dfs(arr, node, level): # go through each node, calc the sum and count of nodes on the same level
            if node:
                if level == len(arr):
                    arr.append([node.val, 1]) # [sum of current level, cnt]
                else: 
                    arr[level][0] += node.val
                    arr[level][1] += 1 
                dfs(arr, node.left, level+1)
                dfs(arr, node.right, level+1)
        
        arr = []
        dfs(arr, root, 0)
        return [total/cnt for total, cnt in arr]
        
                

       
# previous solution 

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def averageOfLevels(self, root: TreeNode) -> 'List[float]':
#         def dfs(hmp, node, level):
#             if level not in hmp:
#                 hmp[level] = []
#             hmp[level].append(node.val)
#             if node.left:
#                 dfs(hmp, node.left, level+1)
#             if node.right:
#                 dfs(hmp, node.right, level+1)
#         if root == None:
#             return []
#         hmp = {}
#         dfs(hmp, root, 0)
#         for k, v in hmp.items():
#             hmp[k] = sum(v)/len(v)
#         return [hmp[k] for k in sorted(hmp.keys())]



# previous solution


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
#         def flat(output, node, level):
#             if level >= len(output):
#                 output.append([])
#             if node.left == node.right == None:
#                 output[level-1].append(node.val)
#             else:
#                 output[level-1].append(node.val)
#                 if node.left:
#                     flat(output, node.left, level+1)
#                 if node.right:
#                     flat(output, node.right, level+1)      
        
#         if root == None: return []
#         else:
#             output = []
#             flat(output, root, 1)
#             print(output)
#             res = [sum(o)/len(o) for o in output if o]
#             return res

