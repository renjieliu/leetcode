# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> 'List[int]':
        if root == None:return []
        output= []
        def look(node, currentLayer, output):
            if node:
                if currentLayer == len(output):
                    output.append(node.val)
                look(node.right, currentLayer+1, output) #look right first
                look(node.left, currentLayer+1, output) # if not there, then look on left
        look(root, 0, output)
        return output