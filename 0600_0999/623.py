# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def flat(hmp, node, index, currLayer, d): #find all the node on that layer and store in a hashmap
            if currLayer == d:
                hmp[index] = node
            elif currLayer < d:
                if node.left:
                    flat(hmp, node.left, index*2+1, currLayer+1, d)
                if node.right:
                    flat(hmp, node.right, index*2+2, currLayer+1, d)

        hmp = {}
        flat(hmp, root, 0, 1, d) #starting at layer 1
        def add(hmp, node, index, currLayer, d, v):
            if currLayer == d-1: #reach the parent layer, create new nodes, and attach old nodes to the new ones
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                if 2*index+1 in hmp:
                    node.left.left = hmp[2*index+1]
                if 2*index+2 in hmp:
                    node.right.right = hmp[2*index+2]

            elif currLayer < d-1:
                if node.left:
                    add(hmp, node.left, index*2+1, currLayer+1, d, v)
                if node.right:
                    add(hmp, node.right, index*2+2, currLayer+1, d, v)

        if d == 1 : # if to add at level 1, just create a new root, and return that
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        else:
            add(hmp, root, 0, 1, d, v)
            return root











