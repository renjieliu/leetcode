# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def flat(output, node, low, high):
            if low<=node.val<=high:
                output.append(node.val)
            if node.left:
                flat(output, node.left, low, high)
            if node.right:
                flat(output, node.right, low, high)

        def buildTree(arr, node, low, high):
            if arr and low <= arr[0] <= node.val:
                node.left = TreeNode(arr[0])
                arr.pop(0)
                buildTree(arr, node.left, low, node.val)
            if arr and node.val <= arr[0] <= high :
                node.right = TreeNode(arr[0])
                arr.pop(0)
                buildTree(arr, node.right, node.val, high)


        output = []
        flat(output, root, low, high)
        if output == []:
            return None
        else:
            start = TreeNode(output.pop(0))
            node = start
            buildTree(output, node, low, high)
            return start










