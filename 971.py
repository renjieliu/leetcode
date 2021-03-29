# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: 'List[int]') -> 'List[int]':
        def dfs(output, node, arr):
            arr.pop(0)
            if node.left:
                if arr[0]==node.left.val: # if same with the first element of arr, pop it
                    dfs(output, node.left, arr)
                elif node.right and arr[0] == node.right.val: # swap left and right
                    output.append(node.val)
                    t = node.left
                    node.left = node.right
                    node.right = t
                    dfs(output, node.left, arr)

            if node.right:
                if arr[0] == node.right.val:
                    dfs(output, node.right, arr)

        output = []
        if root.val == voyage[0]:
            dfs(output, root, voyage)
            return [-1] if voyage else output # voyage is all popped, the tree is traversed w/o issue
        else:
            return [-1]

