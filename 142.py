# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: 'ListNode') -> ListNode:
        hmp = set()
        while head:
            if head in hmp:
                return head
            else:
                hmp.add(head)
                head = head.next
        return None



