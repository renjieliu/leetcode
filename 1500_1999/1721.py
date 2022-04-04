# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: 'Optional[ListNode]', k: int) -> 'Optional[ListNode]': #O(N | 1)
        cnt = 0 
        node = head
        while node:
            cnt += 1 
            if cnt == k :
                a = node
                b = head # set b as head. when total node reaches end, b is at the -k location. (total = k + total-k)
            if cnt > k:
                b = b.next
            node = node.next
        a.val, b.val = b.val, a.val #swap a and b 
        return head
            
        
        
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: #O(N | 1)
#         def helper(node, lvl, k, targetNodes):
#             if node == None:
#                 return 0
#             else:
#                 if lvl == k: #store current value as v[0]
#                     targetNodes[0] = node
#                 nxt = helper(node.next, lvl+1, k, targetNodes)
                
#                 if nxt == k-1: #from the bottom, need to put 
#                     targetNodes[1] = node
                
#                 return nxt + 1
        
#         targetNodes = [None, None]
#         helper(head, 1, k, targetNodes)
#         targetNodes[0].val, targetNodes[1].val = targetNodes[1].val, targetNodes[0].val #swap the 2 values
#         return head
    
 


# previous solution

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapNodes(self, head: ListNode, k: int) -> ListNode:
#         curr = head
#         cnt = 0
#         b = None
#         while curr:
#             cnt +=1
#             if cnt == k:
#                 a = curr #is the left pointer
#                 b = head
#             curr = curr.next
#             if cnt > k: #move b, and so the distance b and curr is k, once curr is at the end of list, b is at end-k position
#                 b = b.next
#         b.val, a.val = a.val, b.val
#         return head


# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapNodes(self, head: ListNode, k: int) -> ListNode:
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         a = k-1
#         b = -k
#         t=arr[a]
#         arr[a] = arr[b]
#         arr[b] = t
#         #print(arr)
#         start = ListNode(arr.pop(0))
#         node = start
#         while arr:
#             node.next = ListNode(arr.pop(0))
#             node = node.next
#         return start


# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapNodes(self, head: ListNode, k: int) -> ListNode:
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         arr[k-1], arr[-k] = arr[-k], arr[k-1]
#         start = ListNode(arr.pop(0))
#         node = start
#         while arr:
#             node.next = ListNode(arr.pop(0))
#             node = node.next
#         return start