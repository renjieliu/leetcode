"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def helper(seen, node):
            if node in seen:
                return seen[node]
            else:
                if node == None:
                    seen[node] = None
                    return seen[node]
                else:
                    curr = Node(node.val, None, None)
                    seen[node] = curr
                    curr.next = helper(seen, node.next)
                    curr.random = helper(seen, node.random)
                    return seen[node]
        seen = {}
        return helper(seen, head)
