"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head == None:
            node = Node(insertVal)
            node.next = node
            return node
        else:
            node = head
            prev = None
            minn = float('inf')
            maxx = -float('inf')
            while node:
                minn = min(minn, node.val)
                maxx = max(maxx, node.val)
                if node.val <= insertVal:
                    prev = node
                elif node.val > insertVal:
                    if prev != None:
                        insertNode = Node(insertVal)
                        insertNode.next = prev.next
                        prev.next = insertNode
                        return head

                if node.next == head:
                    break
                else:
                    node = node.next

            if insertVal <= minn:  # the insert value is <= minn, need to find the location to insert it.
                node = head
                while node:
                    if node.val == minn:
                        if prev != None:
                            insertNode = Node(insertVal)
                            insertNode.next = prev.next
                            prev.next = insertNode
                            return head
                        else:
                            insertNode = Node(insertVal)
                            insertNode.next = node
                            while node.next != head:
                                node = node.next
                            node.next = insertNode
                            return insertNode

                    prev = node
                    node = node.next

            elif insertVal >= maxx:  # the insert value is >= maxx, need to find the location to insert it.
                node = head
                while node:
                    if node.val == maxx:
                        while node.next.val == maxx and node.next != head:
                            node = node.next
                        insertNode = Node(insertVal)
                        insertNode.next = node.next
                        node.next = insertNode
                        return head

                    node = node.next

                    # if cannot be placed within the loop
            insertNode = Node(insertVal)
            insertNode.next = node.next
            node.next = insertNode
            return head












