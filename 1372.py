# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        output = []

        def dfs(node, output, cnt, direction):  # direction: 0 root. 1 left, 2 right
            if node:
                if node.left == node.right == None:  # the leaf node
                    output.append(cnt)  # record the current path length
                else:
                    if direction == 0:  # root
                        if node.left != None:
                            dfs(node.left, output, cnt + 1, 1)
                        if node.right != None:
                            dfs(node.right, output, cnt + 1, 2)
                    elif direction == 1:
                        if node.right != None:
                            dfs(node.right, output, cnt + 1, 2)
                        else:
                            output.append(cnt)  # the path ends here
                        if node.left != None:
                            dfs(node.left, output, 1, 1)  # use current node as the root and check next
                    elif direction == 2:
                        if node.left != None:
                            dfs(node.left, output, cnt + 1, 1)
                        else:
                            output.append(cnt)  # the path ends here
                        if node.right != None:
                            dfs(node.right, output, 1, 2)  # use current node as the root and check next

        if root == None: return 0
        output = []
        dfs(root, output, 0, 0)  # if the root node is not None, at least 1 node in the zigzag path
        return max(output)



