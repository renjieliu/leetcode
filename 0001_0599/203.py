# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: 'Optional[ListNode]', val: int) -> 'Optional[ListNode]':
        while head and head.val == val:
            head = head.next
        if head == None:
            return None
        start = head 
        prev = head 
        head = head.next
        while head:
            if head.val != val:
                prev.next = head 
                prev = head 
            head = head.next
        
        prev.next = None #to avoid the last node.val = val. prev at the end of iteration should be the last node.
        return start
        
        

# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         while head and head.val == val:
#             head = head.next
#         if head == None: return None
#         start = ListNode(head.val)
#         node = start
#         head = head.next
#         while head:
#             if head.val != val:
#                 node.next = ListNode(head.val)
#                 node = node.next
#             head = head.next
#         return start