# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1

        if l1.val <= l2.val:
            start = ListNode(l1.val)
            l1 = l1.next
        else:
            start = ListNode(l2.val)
            l2 = l2.next

        node = start
        while l1 and l2:
            if l1.val<=l2.val:
                node.next = ListNode(l1.val)
                node = node.next
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                node = node.next
                l2 = l2.next

        node.next = l1 if l1 else l2
        return start















