# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
        flat = []
        for l in lists:
            while l:
                flat.append(l.val)
                l = l.next
        flat.sort()
        if len(flat) == 0: return None
        start = ListNode(flat.pop(0))
        node = start
        while flat:
            node.next = ListNode(flat.pop(0))
            node = node.next
        return start

