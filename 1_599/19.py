# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        if n == 1 :
            arr = arr[:-n]
        else:
            arr = arr[:-n] + arr[-n+1:]
        if arr == []:
            return None
        s = ListNode(arr.pop(0))
        node = s
        while arr:
            node.next = ListNode(arr.pop(0))
            node = node.next
        return s