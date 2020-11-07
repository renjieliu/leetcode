# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        A = ""
        while l1:
            A += str(l1.val)
            l1 = l1.next
        B = ""
        while l2:
            B += str(l2.val)
            l2 = l2.next
        res = str(int(A) + int(B))
        start = ListNode(int(res[0]))
        node = start
        for r in res[1:]:
            node.next = ListNode(int(r))
            node = node.next
        return start


