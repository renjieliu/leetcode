# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> 'List[int]':
        def flat(output, node):
            if node:
                if node.left == node.right ==None:
                    output.append(node.val)
                else:
                    output.append(node.val)
                    if node.left != None:
                        flat(output, node.left)
                    if node.right != None:
                        flat(output, node.right)
        output_1  = []
        output_2  = []
        flat(output_1, root1)
        flat(output_2, root2)
        return sorted(output_1+output_2)