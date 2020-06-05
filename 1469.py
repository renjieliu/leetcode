# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getLonelyNodes(self, root: TreeNode) -> 'List[int]':
        def flat(output, node):
            if node.left == node.right == None :
                return None
            else:
                if node.left:
                    if node.right == None:
                        output.append(node.left.val)
                    flat(output, node.left)
                if node.right:
                    if node.left == None:
                        output.append(node.right.val)
                    flat(output, node.right)
        output = []
        flat(output, root)
        return output




