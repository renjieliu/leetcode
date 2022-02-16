# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        def helper(output, node, prevprev, prev, i): # Time:O(n) + Space O(1) recursive approach
            if node:
                if i % 2: #the odd node
                    if prevprev: # point the prevprev next to current
                        prevprev.next = node
                    else:
                        output[0] = node #current node becomes the head to return
                    prev.next = node.next #swap current node with prev
                    node.next = prev
                    helper(output, prev.next, node, prev,i+1)
                else:
                    helper(output, node.next, prev, node, i+1)
                
        output = [None]
        helper(output, head, None, None, 0)
        if output[0]:
            return output[0]
        else:
            return head


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution: #the flat and generate approach, Time: O(N) + Space: O(N)
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None:
#             return None
#         arr = []
#         while head: #flat the head, and swap the last 2 values, if current length is even
#             arr.append(head.val)
#             if len(arr) % 2 == 0:
#                 arr[-1], arr[-2] = arr[-2], arr[-1]
#             head = head.next
        
#         root = ListNode(arr[0])  #constuct the new root
#         node = root
#         for i in range(1, len(arr)):
#             node.next = ListNode(arr[i])
#             node = node.next
#         return root 




# previous approach

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if head == None: return None
#         arr = []
#         cnt = 0
#         while head:
#             arr.append(head.val)
#             if len(arr) % 2 == 0:
#                 arr = arr[:-2] + [arr[-1]] + [arr[-2]]
#             head = head.next

#         output = ListNode(arr.pop(0))
#         start = output
#         while arr:
#             output.next = ListNode(arr.pop(0))
#             output = output.next
#         return start



# previous approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def swapPairs(self, head: 'ListNode') -> 'ListNode':
#         if head == None: return head        
#         node = head
#         arr = []
#         while node:
#             arr.append(node.val) 
#             node = node.next
#         for i, c in enumerate(arr):
#             if i%2 == 1:
#                 arr[i-1], arr[i] = arr[i], arr[i-1]
#         output = ListNode(arr[0])
#         node = output
#         for i in range(1, len(arr)):
#             node.next = ListNode(arr[i])
#             node = node.next
#         return output




