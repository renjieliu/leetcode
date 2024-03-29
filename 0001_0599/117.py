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
    def connect(self, root: 'Node') -> 'Node': #RL 20220513: Copied Solution. O(N | 1)
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next
               
        return root
    


# previous solution

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
#         def helper(node, hmp,
#                    level):  # check the right node first, push into a stk, when same level node comes, populate the next from the stk.
#             if level in hmp:
#                 if hmp[level]:
#                     node.next = hmp[level].pop(0)
#                     hmp[level].append(node)
#             else:
#                 hmp[level] = [node]

#             if node.right:
#                 helper(node.right, hmp, level + 1)
#             if node.left:
#                 helper(node.left, hmp, level + 1)

#         if root == None: return None
#         helper(root, {}, 0)
#         return root

