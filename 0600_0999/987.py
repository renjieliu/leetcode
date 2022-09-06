# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: 'Optional[TreeNode]') -> 'List[List[int]]': # O( (NlogN)**2 | N )
        def helper(hmp, node, col, row): # go through all the nodes in the tree, and record the col and row to hmp
            if node:
                if col not in hmp:
                    hmp[col] = [[row,node.val]]
                else:
                    hmp[col].append([row, node.val])
                helper(hmp, node.left, col-1, row+1)
                helper(hmp, node.right, col+1, row+1)
        
        hmp = {}
        helper(hmp, root, 0, 0)
        output = []
        for k in sorted(hmp.keys()): # sort the col
            output.append([])
            arr = sorted(hmp[k]) # sort the row and val
            for row, val in arr:
                output[-1].append(val)
        return output
    


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def verticalTraversal(self, root: TreeNode) -> 'List[List[int]]':
#         def flat(hmp, x, y, node):
#             hmp[x].append([y, node.val])
#             if node.left:
#                 flat(hmp, x-1, y-1, node.left)
#             if node.right:
#                 flat(hmp, x+1, y-1, node.right)
#         hmp = defaultdict(list)
#         flat(hmp, 0,0,root)
#         output = []
#         for k in sorted(hmp.keys()): #sort by y and value
#             hmp[k].sort(key=lambda x: (x[0], -x[1]), reverse = True) #revese the x[1], to sort ascendingly
#             #print(hmp[k])
#             output.append([])
#             for v in hmp[k]:
#                 output[-1].append(v[1])
#         return output




# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def verticalTraversal(self, root: TreeNode) -> 'List[List[int]]':
#         def dfs(hmp, index, level, node):
#             if node.left == node.right == None:
#                 position = (index[0], index[1], level)
#                 if position not in hmp:
#                     hmp[position] = []
#                 hmp[position].append(node.val)
#             else:
#                 position = (index[0], index[1], level)
#                 if position not in hmp:
#                     hmp[position] = []
#                 hmp[position].append(node.val)
#                 if node.left:
#                     dfs(hmp, [index[0] - 1, index[1] - 1], level + 1, node.left)
#                 if node.right:
#                     dfs(hmp, [index[0] + 1, index[1] - 1], level + 1, node.right)
#
#         hmp = {}
#         dfs(hmp, [0, 0], 0, root)
#         k_list = sorted(hmp.keys(), key=lambda x: x[1], reverse=True)  # sorted by y
#         k_list = sorted(k_list, key=lambda x: x[0])  # sort by x
#         # print(k_list)
#
#         output = []
#         prev = k_list[0][0]
#         temp = sorted(hmp[k_list[0]])  # sort by the values
#         for k in k_list[1:]:
#             if k[0] == prev:
#                 temp += sorted(hmp[k])
#             else:
#                 output.append(temp)
#                 temp = sorted(hmp[k])
#                 prev = k[0]
#
#         output.append(temp)
#         return output
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
#
#
