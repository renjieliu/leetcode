# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None: return None
        even = []
        odd = []
        p = 0
        while head:
            if p % 2 == 0:
                even.append(head.val)
            else:
                odd.append(head.val)
            head = head.next
            p += 1
        head = ListNode(even.pop(0))
        node = head
        while even:
            node.next = ListNode(even.pop(0))
            node = node.next
        while odd:
            node.next = ListNode(odd.pop(0))
            node = node.next
        return head

