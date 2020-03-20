# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> 'List[int]':
        def flat(output, node):
            if node.left == node.right ==None:
                output.append(node.val)
            else:
                if node.left != None:
                    flat(output, node.left)
                output.append(node.val)
                if node.right !=None:
                    flat(output, node.right)

        output = []
        if root == None: return output
        else:
            flat(output, root)
        return output