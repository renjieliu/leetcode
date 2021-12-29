# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        def dfs(output, level, node): 
            A = B = level
            if node.left:
                A = max(A, dfs(output, level+1, node.left)) #deepest level of the left child
            if node.right:
                B = max(B, dfs(output, level+1, node.right)) #deepest level of the right child
            # print(node.val, A, B)
            if A==B:
                if A >= output[0]: #either A or B >= visited deepest 
                    output[0] = A
                    output[1] = node
            return max(A, B)
        output = [-float('inf'), None]
        dfs(output, 0, root)
        # print(output)
        return output[1]
        
        

        