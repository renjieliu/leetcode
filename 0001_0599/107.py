# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> 'List[List[int]]':
        def dfs(node, level, path):
            if node.left == node.right == None:
                return
            else:
                if node.left:
                    if level + 1 >= len(path):
                        path.append([])
                    path[level + 1].append(node.left.val)
                    dfs(node.left, level + 1, path)
                if node.right:
                    if level + 1 >= len(path):
                        path.append([])
                    path[level + 1].append(node.right.val)
                    dfs(node.right, level + 1, path)

        if root == None: return []
        path = [[root.val]]  # each level values from left to right
        dfs(root, 0, path)
        return path[::-1]

