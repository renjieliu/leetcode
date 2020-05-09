# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if head == None: return None
        start = ListNode(head.val)
        node = start
        head = head.next
        while head:
            if head.val != val:
                node.next = ListNode(head.val)
                node = node.next
            head = head.next
        return start