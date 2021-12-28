# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        arr = []
        while head: #flat, transform according to the problem description, form a new linked list, and return the new head
            arr.append(head.val)
            head = head.next 
        stk = []
        g = 0 
        p = 0
        while p < len(arr):
            g = g+1
            rem = len(arr)-p
            if (g < rem and g % 2 == 0) or (g >= rem and (rem) % 2 == 0): # even group length or the last group 
                stk += arr[p:p+g][::-1]
            else:
                stk += arr[p:p+g]
            p+=g
        
        stk = deque(stk)
        start = ListNode(stk.popleft()) 
        node = start
        while stk:
            node.next = ListNode(stk.popleft())
            node = node.next
        return start
    
    
