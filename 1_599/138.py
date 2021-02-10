# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def helper(seen, original):
            if original in seen:
                return seen[original]
            else:
                if original== None:
                    seen[original] = original
                    return seen[original]
                else:
                    copied = Node(original.val, None, None)
                    seen[original] = copied
                    copied.next = helper(seen, original.next)
                    copied.random = helper(seen, original.random)
                    return copied

        return helper({}, head)