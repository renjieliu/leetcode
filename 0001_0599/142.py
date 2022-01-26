# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        fast = head 
        slow = head
        while fast: # Floyd's tortoise and hare's algorithm
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else: # no cycle found
                return None
            
            if fast == slow:
                break
            
         
        if fast == None:
            return None

        slow = head  # move the slow back to the head. The meet point will be the start of the cycle when they meet again.
        
        while fast!=slow:
            slow = slow.next
            fast = fast.next
        
        return slow
            



# previous approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
#         fast = head 
#         slow = head
#         while fast: # Floyd's tortoise and hare algo
#             if fast.next:
#                 fast = fast.next.next
#             else:
#                 return None
#             slow = slow.next
#             if fast == slow:
#                 break
#         if fast == None: 
#             return None
#         slow = head #let fast finish current loop, and slow move from the start. They will meet at the cycle point
#         while fast != slow: 
#             fast = fast.next
#             slow = slow.next
#         return fast

        

        
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         seen = set()
#         while head: # just to check if current node was seen
#             if head not in seen:
#                 seen.add(head)
#                 head = head.next
#             else:
#                 return head
#         return None





# previous approach

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: 'ListNode') -> ListNode:
#         hmp = set()
#         while head:
#             if head in hmp:
#                 return head
#             else:
#                 hmp.add(head)
#                 head = head.next
#         return None



