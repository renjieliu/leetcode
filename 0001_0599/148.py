# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def flat(output, node):
            while node:
                output.append(node.val)
                node = node.next

        output = []
        flat(output, head)
        output.sort()
        if output == []:
            return None
        start = ListNode(output.pop(0))
        node = start
        while output:
            node.next = ListNode(output.pop(0))
            node = node.next
        return start
