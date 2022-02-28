# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        start = ListNode(None)
        head = head.next #take out the first 0 of the ListNode
        node = start
        total = 0 # to record the segment sum
        while head:
            if head.val == 0: # reached the end of the current segment
                node.next = ListNode(total)
                node = node.next
                total = 0
            else:
                total += head.val
            head = head.next
        return start.next

    
    

