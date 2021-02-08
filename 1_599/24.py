# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None: return None
        arr = []
        cnt = 0
        while head:
            arr.append(head.val)
            if len(arr) % 2 == 0:
                arr = arr[:-2] + [arr[-1]] + [arr[-2]]
            head = head.next

        output = ListNode(arr.pop(0))
        start = output
        while arr:
            output.next = ListNode(arr.pop(0))
            output = output.next
        return start


