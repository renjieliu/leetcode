# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(curr, path, node):
            if node.left == node.right == None:
                path.append((curr + [node.val])[::-1])
            else:
                if node.left != None:
                    dfs(curr + [node.val], path, node.left)
                if node.right != None:
                    dfs(curr + [node.val], path, node.right)

        path = []
        dfs([], path, root)
        path.sort()
        output = ""
        for c in path[0]:
            output += chr(c + 97)
        return output

