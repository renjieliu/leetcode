# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        else:
            stk = []
            while head != None:
                stk.append(head.val)
                head = head.next
            if stk == []:
                return None
            else:
                k = k % len(stk)
                arr = stk[-k:].copy() + stk[:-k].copy()
                output = ListNode(arr[0])
                arr.pop(0)
                node = output
            while arr:
                node.next = ListNode(arr.pop(0))
                node = node.next
            return output





