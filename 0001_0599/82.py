# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return None
        start = None
        prev = head.val
        cnt = 1
        head = head.next
        while head:
            if head.val == prev:
                cnt+=1
            else: # current value differ from the previous
                if cnt == 1: #prev repeating once, need prev as a node
                    if start == None:
                        start = ListNode(prev)
                        node = start
                    else:
                        node.next = ListNode(prev)
                        node = node.next
                    prev = head.val
                    cnt = 1
                else: #prev repeating more than once
                    prev = head.val
                    cnt = 1

            head = head.next

        if cnt == 1:
            if start == None:
                start = ListNode(prev)
            else:
                node.next = ListNode(prev)
                node = node.next

        return start



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