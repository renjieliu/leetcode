# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None: return None
        flat = []
        while head:
            flat.append(head.val)
            head = head.next
        left = []
        right = []
        while flat:
            if flat[0] < x:
                left.append(flat.pop(0))
            else:
                right.append(flat.pop(0))
        pool = left + right
        start = ListNode(pool.pop(0))
        node = start
        while pool:
            node.next = ListNode(pool.pop(0))
            node = node.next
        return start
