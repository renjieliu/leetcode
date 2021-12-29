"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None: 
            return None 
        else:
            hmp = {}
            def flat(hmp, idx, node): #flat the tree, to record all the nodes
                hmp[idx] = node
                if node.left: flat(hmp, idx*2+1, node.left)
                if node.right: flat(hmp, idx*2+2, node.right)
            
            def helper(hmp, idx, node, level): # point the nodes to the next
                if idx < 2**level-2: # if it's not the last nodes on the level
                    node.next = hmp[idx+1]
                if node.left:
                    helper(hmp, idx*2+1, node.left, level+1)
                if node.right:
                    helper(hmp, idx*2+2, node.right, level+1)
            
            flat(hmp, 0, root)
            helper(hmp, 0, root, 1)
            
            return root
        
        



# previous approach
# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """


# class Solution:
#     def connect(self, root: 'Node') -> 'Node':

#         if root == None: return root

#         def flat(node, idx, lvl):
#             if idx != 2 ** lvl - 2:  # no node on the right
#                 node.next = findNext(idx + 1, root, 0)
#             if node.left:
#                 flat(node.left, idx * 2 + 1, lvl + 1)
#             if node.right:
#                 flat(node.right, idx * 2 + 2, lvl + 1)

#         def findNext(target, node, idx):
#             if idx == target:
#                 return node
#             else:
#                 if node.left:
#                     ans = findNext(target, node.left, 2 * idx + 1)
#                     if ans:
#                         return ans
#                 if node.right:
#                     ans = findNext(target, node.right, 2 * idx + 2)
#                     if ans:
#                         return ans

#         flat(root, 0, 1)
#         return root


















