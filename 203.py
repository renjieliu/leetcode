# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        stk = []
        while head:
            if head.val != val:
                stk.append(head.val)
            head = head.next
        if stk == []:return None
        else:
            start = ListNode(stk.pop(0))
            node = start
            while stk:
                node.next = ListNode(stk.pop(0))
                node = node.next
            return start