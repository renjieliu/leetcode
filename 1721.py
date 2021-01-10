# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        start = ListNode(arr.pop(0))
        node = start
        while arr:
            node.next = ListNode(arr.pop(0))
            node = node.next
        return start