# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: 'ListNode') -> 'ListNode':
        def helper(node):
            beforeAdd = node.val
            if node.next == None:
                node.val += 1
            else:
                node.val += helper(node.next)
            node.val %= 10
            return 1 if node.val == 0 and beforeAdd == 9 else 0  # this is the carry over digit

        if helper(head) == 1:
            newHead = ListNode(1)
            newHead.next = head
            return newHead
        else:
            return head


