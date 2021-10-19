# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        else:
            slow = fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow: #fast meets slow
                    return True
            return False

# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         lkp = set()
#         while head:
#             if head not in lkp:
#                 lkp.add(head)
#                 head = head.next
#             else:
#                 return True
#         return False