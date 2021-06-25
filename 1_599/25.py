# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(node, prev, tail):
            if node == tail: #point the current to the previous one
                node.next = prev
                if prev:
                    prev.next = None
            else:
                reverse(node.next, node, tail) #keep point current to the previous one
                node.next = prev

        node = head
        root = None
        startNode = node
        cnt = 0
        while node:
            cnt += 1
            if cnt % k == 0: #reach the count, and reverse
                successor = node.next
                reverse(startNode, None, node) #startNode of current segment, prev, currentNode as tail
                if root == None:
                    root = node
                else:
                    prevEnd.next = node
                prevEnd = startNode #the startNode becomes the tail after reverse
                startNode.next = successor #connect the next node to the tail of reverse
                cnt = 0
                node = successor #re-assign successor to node
            else:
                node = node.next
            if cnt == 0:
                startNode = node #current node as startNode

        if cnt > 0: #the remaining items not reversed [1,2,3,4,5], reverse every 2 items will leave node 5 in the end.
            prevEnd.next = startNode
        return root



