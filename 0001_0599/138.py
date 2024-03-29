"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def helper(copied, node):
            if node == None:
                return None
            elif node in copied: # the node is copied
                return copied[node]
            else:
                newNode = Node(node.val) # create the new node, and add to the hashmap
                copied[node] = newNode
                
                newNode.next = helper(copied, node.next) #work on the next pointer
                newNode.random = helper(copied, node.random) # work on the random pointer
                return newNode
        
        return helper({}, head)
        

        
        
# previous approach

# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         def copy(copied_set, node):
#             if node in copied_set:
#                 return copied_set[node]
#             else:
#                 if node == None:
#                     copied_set[node] = None
#                     return copied_set[node]
#                 else:
#                     copied = Node(node.val)
#                     copied_set[node] = copied
#                     copied.next = copy(copied_set, node.next)
#                     copied.random = copy(copied_set, node.random)
#                     return copied
#         return copy({}, head)


# previous approach

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
#
#
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         def helper(seen, original):
#             if original in seen:
#                 return seen[original]
#             else:
#                 if original== None:
#                     seen[original] = original
#                     return seen[original]
#                 else:
#                     copied = Node(original.val, None, None)
#                     seen[original] = copied
#                     copied.next = helper(seen, original.next)
#                     copied.random = helper(seen, original.random)
#                     return copied
#
#         return helper({}, head)