# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def helper(node, target):
            if node == None: return None

            if node.val == target:
                if node.left == node.right == None:
                    return None
                elif node.left and node.right == None:
                    return node.left
                elif node.right and node.left == None:
                    return node.right
                else:
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    node.val = curr.val
                    node.right = helper(node.right, curr.val)

            elif node.val > target:
                node.left = helper(node.left, target)
            elif node.val < target:
                node.right = helper(node.right, target)

            return node

        node = helper(root, key)

        return node

