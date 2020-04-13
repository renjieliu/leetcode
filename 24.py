# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None: return head
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        for i, c in enumerate(arr):
            if i % 2 == 1:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        output = ListNode(arr[0])
        node = output
        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return output

