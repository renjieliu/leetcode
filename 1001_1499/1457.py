# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: 'Optional[TreeNode]') -> int: # O( N | 10 )
        def dfs(output, cnt, node):  #check all the paths, and check if the current path is palindromic
            if node: 
                cnt[node.val] += 1 # add the slot by 1 
                if node.left == node.right == None:
                    output[0] += len([c for c in cnt if c%2]) <= 1 # to check if more than 1 odd-time occurrence
                else:
                    dfs(output, cnt, node.left)
                    dfs(output, cnt, node.right)
                cnt[node.val] -= 1
        
        output = [0] 
        dfs(output, [0] * 10 , root)  # initialize the cnt as [0]*10, as the number range is 1-9 
        return output[0]
    


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def pseudoPalindromicPaths(self, root: TreeNode) -> int:
#         def flat(output, curr, node):
#             if node.val not in curr:
#                 curr[node.val] = 0
#             curr[node.val] += 1
#             if node.left == node.right == None:
#                 odd = 0
#                 for k, v in curr.items():
#                     odd += 1 if v % 2 else 0
#                 output[0] += 1 if odd <= 1 else 0
#             else:
#                 if node.left:
#                     flat(output, curr, node.left)
#                 if node.right:
#                     flat(output, curr, node.right)

#             curr[node.val] -= 1
#             if curr[node.val] == 0:
#                 del curr[node.val]

#         output = [0]
#         flat(output, {}, root)
#         return output[0]



