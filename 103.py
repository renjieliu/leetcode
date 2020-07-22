# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> 'List[List[int]]':
        def flat(output, level, node):
            if level >= len(output):
                output.append([])
            if node.left==node.right ==None:
                output[level].append(node.val)
            else:
                output[level].append(node.val)
                if node.left:
                    flat(output, level+1 , node.left)
                if node.right:
                    flat(output, level+1, node.right)
        if root == None: return []
        else:
            output = []
            flat(output, 0, root)
            i = 0
            while i < len(output):
                if i%2 != 0:
                    output[i] = output[i][::-1]
                i+=1
            return output
