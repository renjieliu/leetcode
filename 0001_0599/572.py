# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: 'Optional[TreeNode]', subRoot: 'Optional[TreeNode]') -> bool: #O(N2), this should not be the optimal approach
        def flat(output, node): # need to add all the sub nodes to the output, even if it's None
            output.append(node.val)
            if node.left == None:
                output.append(None)
            else:
                flat(output, node.left)
            if node.right == None:
                output.append(None)
            else:
                flat(output, node.right)
        p1 = []
        p2 = []
        flat(p1, root)
        flat(p2, subRoot)
        # print(p1, p2)
        for i in range(len(p1)): #check if the tree from current node is same as subRoot
            if p1[i:i+len(p2)] == p2:
                return True
        return False
    
    
        
            
            