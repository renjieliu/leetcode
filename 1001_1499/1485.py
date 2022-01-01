# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def helper(node, newNode, idx, hmp, rmd): #build the skeleton of the new tree, and find the random pointer location
            hmp[node] = idx #the index of the node
            rmd[idx] = newNode
            if node.left:
                newNode.left = NodeCopy(node.left.val) #copy the left node
                helper(node.left, newNode.left, idx*2+1, hmp, rmd)
            if node.right:
                newNode.right = NodeCopy(node.right.val) #copy the right node
                helper(node.right, newNode.right, idx*2+2, hmp, rmd)
        
        def findRandom(node, newNode, idx, hmp, rmd):
            if node.random: #find the random pointer node 
                newNode.random = rmd[hmp[node.random]] #find the random pointer node with index
            if node.left:
                findRandom(node.left, newNode.left, idx*2+1, hmp, rmd)
            if node.right:
                findRandom(node.right, newNode.right, idx*2+2, hmp, rmd)
        
        if root == None:
            return None
        
        hmp = {}
        rmd = {}
        newNode = NodeCopy(root.val)
        helper(root, newNode, 0, hmp, rmd)  
        findRandom(root, newNode, 0, hmp, rmd)
        
        return newNode
                
