# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: 'Optional[TreeNode]') -> 'List[List[int]]': #O( N2logN | N )
        def helper(hmp, level, col, node): # col is to record current column number
            if node:
                hmp[col].append([level, node.val])
                helper(hmp, level+1, col-1, node.left) # add the left node first, according to the requirement.
                helper(hmp, level+1, col+1, node.right)
        
        hmp = defaultdict(lambda : [])
        helper(hmp, 0, 0, root) # the column number for the root should be 0
        output = []
        lst = sorted(hmp.keys())  # O(NlogN)
        # print(hmp)
        for k in lst: #O(N * NlogN) ==> N2logN
            output.append( [nodes for level, nodes in sorted(hmp[k], key = lambda x: x[0]) ] ) # sort the nodes by level
        return output

            
