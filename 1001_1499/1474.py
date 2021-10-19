# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = head
        node = head.next
        cnt = 1
        toss = 0
        while node:
            if cnt < m:
                prev.next = ListNode(node.val)
                prev = prev.next
                cnt += 1
                toss = 0
            elif cnt == m:
                if toss < n:
                    toss += 1
                    if toss == n:
                        cnt = 0
                        toss = 0
            node = node.next
        return head




