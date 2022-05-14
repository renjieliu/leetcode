# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0 
    
    def averageOfSubtree(self, root: 'Optional[TreeNode]') -> int: # O(N | 1)
        def helper(node): 
            if node:
                if node.left == node.right == None:
                    self.cnt += 1 
                    return [node.val, 1] #[sumOfSubTree, subTreeNodeCount]
                A = helper(node.left)
                B = helper(node.right)
                totalCnt = (1 + A[1] + B[1]) 
                total = (node.val + A[0] + B[0])
                self.cnt += 1 if node.val == total // totalCnt else 0 
                return [total, totalCnt] #[sumOfSubTree, subTreeNodeCount] 
            else: 
                return [0, 0]
        
        helper(root)
        return self.cnt
                    
                

