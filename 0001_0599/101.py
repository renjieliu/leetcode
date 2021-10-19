# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: #read from left to right, and read from right to left, see if the path is the same
        def dfs(node, path, direction):
            if node.left == node.right==None:
                path[-1].append(node.val)
            else:
                path[-1].append(node.val)
                if direction == 1: #left first
                    if node.left!=None:
                        dfs(node.left, path, direction)
                    else:
                        path[-1].append(None)
                    if node.right!=None :
                        dfs(node.right, path, direction)
                    else:
                        path[-1].append(None)
                else: #right first
                    if node.right!=None :
                        dfs(node.right, path, direction)
                    else:
                        path[-1].append(None)
                    if node.left!=None:
                        dfs(node.left, path, direction)
                    else:
                        path[-1].append(None)
        if root == None: return True
        else:
            path=[[]]
            dfs(root, path, 1)
            path.append([])
            dfs(root, path, 2)
            print(path)
            return True if path[0] == path[1] else False
