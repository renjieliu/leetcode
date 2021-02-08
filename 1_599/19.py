# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        flat = []
        node = head
        while node:
            flat.append(node.val)
            node = node.next
        takeOut = len(flat)-n
        flat = flat[:takeOut] + flat[takeOut+1:]
        if flat == []: return None
        else:
            start = ListNode(flat[0])
            node = start
            for i in range(1, len(flat)):
                node.next = ListNode(flat[i])
                node = node.next
            return start