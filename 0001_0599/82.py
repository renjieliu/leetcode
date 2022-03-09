# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]': #O(N | 1)
        if head == None:
            return head 
        else:
            start = ListNode() #dummy start node, will need to return start.next
            node = start
            prevVal = head.val 
            prevNode = head 
            prevCnt = 1
            head = head.next
            while head:
                if head.val != prevVal:
                    if prevCnt == 1: #if prev Node count is 1
                        node.next = prevNode
                        node = node.next 
                    prevVal = head.val
                    prevNode = head
                    prevCnt = 1
                else: # increment the prevCnt, if current head value is same as previous 
                    prevCnt += 1
                head = head.next

            if prevCnt == 1 : #add the last node
                node.next = prevNode
            else: #cut off the last node
                node.next = None
            
            return start.next
        


# previous approach

# # Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head == None: return None
#         start = None
#         prev = head.val
#         cnt = 1
#         head = head.next
#         while head:
#             if head.val == prev:
#                 cnt+=1
#             else: # current value differ from the previous
#                 if cnt == 1: #prev repeating once, need prev as a node
#                     if start == None:
#                         start = ListNode(prev)
#                         node = start
#                     else:
#                         node.next = ListNode(prev)
#                         node = node.next
#                     prev = head.val
#                     cnt = 1
#                 else: #prev repeating more than once
#                     prev = head.val
#                     cnt = 1

#             head = head.next

#         if cnt == 1:
#             if start == None:
#                 start = ListNode(prev)
#             else:
#                 node.next = ListNode(prev)
#                 node = node.next

#         return start



# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head == None:
#             return None
#         else:
#             node = head
#             curr = node.val
#             cnt = 0
#             start_node = None
#             while node:
#                 pre = curr
#                 curr = node.val
#                 if curr == pre:
#                     cnt += 1
#                 else:
#                     if cnt == 1:
#                         if start_node == None:
#                             start_node = ListNode(pre)
#                             follow_node = start_node
#                         else:
#                             follow_node.next = ListNode(pre)
#                             follow_node = follow_node.next
#                         cnt = 1
#                     else:
#                         cnt = 1
#                 node = node.next
#
#             if cnt == 1:  # for the last node, to see if it's dups
#                 if start_node == None:
#                     start_node = ListNode(curr)
#                     follow_node = start_node
#                 else:
#                     follow_node.next = ListNode(curr)
#                     follow_node = follow_node.next
#
#             return start_node