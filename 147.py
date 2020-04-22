# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None: return None
        start = ListNode(head.val)
        head = head.next
        while head:
            newNode = ListNode(head.val)
            pre = None
            node = start
            find = 0
            while node:  # find the node location  to insert the current head
                if node.val >= head.val:
                    find = 1
                    if pre == None:  # insert at the beginning
                        currStart = newNode
                        currStart.next = start
                        start = currStart
                    else:
                        pre.next = newNode
                        newNode.next = node
                    break
                pre = node
                node = node.next

            if find == 0:
                pre.next = newNode

            head = head.next

        return start
