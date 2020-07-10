"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node, output):
            if node.child == node.next == None:
                output.append(node.val)
            else:
                output.append(node.val)
                if node.child:
                    dfs(node.child, output)
                if node.next:
                    dfs(node.next, output)

        if head == None:
            return None
        else:
            output = []
            dfs(head, output)
            if len(output) == 1:
                return Node(output[0], None, None, None)
            start = Node(output[0], None, None)
            old = start
            node = start.next
            output.pop(0)
            while output:  # Node(val, prev, next, child)
                node = Node(output[0], old, None, None)
                old.next = node
                old = node
                node = node.next
                output.pop(0)
            return start


















