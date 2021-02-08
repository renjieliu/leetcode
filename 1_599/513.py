# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(node, level, nodeID, output):
            if node.left == node.right == None :
                return
            else:
                if node.left:
                    output.append([level+1, nodeID*2+1, node.left.val])
                    dfs(node.left, level+1, nodeID*2+1, output)
                if node.right:
                    output.append([level+1, nodeID*2+2, node.right.val])
                    dfs(node.right, level+1, nodeID*2+2, output)
        output = [ [0,0, root.val] ] #level, nodeID, val
        dfs(root, 1, 0, output)
        output.sort(key = lambda x: x[1])
        output.sort(key = lambda x: x [0], reverse = True)
        return output[0][2]