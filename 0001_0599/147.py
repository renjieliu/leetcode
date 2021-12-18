# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        start = ListNode(head.val)
        node = start
        head = head.next
        prev = None
        while head: # find the first elements larget than curr, and insert there
            curr = ListNode(head.val)
            find = 0
            node = start
            while node:
                if node.val >= curr.val:
                    find = 1
                    if prev: 
                        prev.next = curr
                        curr.next = node
                    else:
                        start = curr
                        curr.next = node
                    break
                else:
                    prev = node
                    node = node.next
                
            if find == 0:
                prev.next = curr
            prev = None
            head = head.next
        
        return start
                
            


# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         if head == None:return None
#         output_start = ListNode(head.val)
#         head = head.next
#         while head:
#             if head.val <= output_start.val:
#                 currStart = output_start
#                 output_start = ListNode(head.val)
#                 output_start.next = currStart
#             else: #to find a place in the output for the curr head val
#                 prev = node = output_start
#                 find = 0
#                 while node:
#                     if head.val <= node.val:
#                         currNode = ListNode(head.val)
#                         currNode.next = prev.next
#                         prev.next = currNode
#                         find = 1
#                         break
#                     else:
#                         prev = node
#                     node = node.next
#                 if find == 0 : #current val is larger than the last element, append to the end
#                     currNode = ListNode(head.val)
#                     currNode.next = prev.next
#                     prev.next = currNode
#                     find = 1
#             head = head.next
#         return output_start

# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         if head == None: return None
#         start = ListNode(head.val)
#         head = head.next
#         while head:
#             newNode = ListNode(head.val)
#             pre = None
#             node = start
#             find = 0
#             while node:  # find the node location  to insert the current head
#                 if node.val >= head.val:
#                     find = 1
#                     if pre == None:  # insert at the beginning
#                         currStart = newNode
#                         currStart.next = start
#                         start = currStart
#                     else:
#                         pre.next = newNode
#                         newNode.next = node
#                     break
#                 pre = node
#                 node = node.next
#
#             if find == 0:
#                 pre.next = newNode
#
#             head = head.next
#
#         return start
