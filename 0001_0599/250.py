# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def helper(node, output):
            if node.left == node.right == None:
                output[0] += 1
                return True
            else:
                A = B = None  # initialize the left and right to none. and check if left / right side satisfy the condition
                if node.left:
                    if helper(node.left,
                              output) == True and node.val == node.left.val:  # cannot compare the value first, otherwise helper won't run.
                        A = 1
                    else:
                        A = 0
                if node.right:
                    if helper(node.right, output) == True and node.val == node.right.val:
                        B = 1
                    else:
                        B = 0
                if (A == 1 and B == None) or (A == None and B == 1) or (A == 1 and B == 1):
                    output[0] += 1
                    return True
                else:
                    return False

        if root == None:
            return 0
        else:
            output = [0]
            helper(root, output)
            return output[0]

