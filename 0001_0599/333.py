# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: 'Optional[TreeNode]') -> int:
        def helper(output, node): 
            if node.left == node.right == None:
                output[0] = max(output[0], 1)
                return [1, node.val, node.val] #cnt, range of subtree
            else:
                A = B = 0
                minn = maxx = node.val
                valid = 1 
                if node.left:
                    T = helper(output, node.left)
                    if T[1] == None or node.val <= T[1] or node.val <= T[2]:
                        valid = 0
                    else:
                        A = T[0]
                        minn = T[1]
                if node.right:
                    T = helper(output, node.right)
                    # print(node.val, T)
                    if T[1] == None or node.val >= T[1] or node.val >= T[2]:
                        valid = 0 
                    else:
                        B = T[0]
                        maxx = T[2]
                
                if valid == 0:
                    return [0, None, None] #current tree is void
                output[0] = max(output[0], (A+B+1)) 
                ret = [A+B+1, min(node.val, minn), max(node.val, maxx) ] 
                # print(node.val, ret)
                return ret 
        
                    
        if root == None:
            return 0
        else:
            output = [0]
            helper(output, root)
            return output[0]
            
            
           
            
            