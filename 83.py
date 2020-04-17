# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:return None
        else:
            node = head
            start = o_node = ListNode(node.val)
            curr = o_node.val #value of the head
            while node:
                pre = curr
                curr = node.val
                if curr != pre:
                    o_node.next = ListNode(curr)
                    o_node = o_node.next
                node = node.next
            return start