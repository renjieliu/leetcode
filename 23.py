# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
        if lists == []: return None
        flat = []
        for l in lists:
            while l:
                flat.append(l.val)
                l = l.next
        if flat == []: return None
        flat.sort()
        start = ListNode(flat[0])
        node = start
        i = 1
        while i < len(flat):
            node.next = ListNode(flat[i])
            node = node.next
            i += 1
        return start


