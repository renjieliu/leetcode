# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        hmp = defaultdict(int)
        for a in arr:
            hmp[a] +=1
        start = None
        for a in arr:
            if hmp[a] == 1:
                if start==None:
                    start = ListNode(a)
                    node = start
                else:
                    node.next = ListNode(a)
                    node = node.next
        return start
