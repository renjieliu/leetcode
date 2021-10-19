# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head ==None: return None
        node = head
        stk = []
        while node:
            stk.append(node.val)
            node = node.next
        node = head #preserve the head node
        stk.pop(0)
        turn = 1
        while stk:
            node.next = ListNode(stk.pop(-turn))
            turn = abs(turn-1) #1 to 0, 0 to 1
            node = node.next