# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseFirstN(node, follower, n):
            if n == 1 :
                follower[0] = node.next # save the end node's next, this will become the first node's next
                return node
            else:
                output = reverseFirstN(node.next, follower, n-1) #reverse the following nodes
                node.next.next = node
                node.next = follower[0] #first node's next
                return output
        if left == 1:
            return reverseFirstN(head, [None], right)
        else:
            head.next = self.reverseBetween(head.next, left-1, right-1)
            return head

# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         nxt_ptr = [None]
#         def reverseFirstN(node, nxt_ptr, n):
#             if n == 1: #this is the last one
#                 nxt_ptr[0] = node.next #save the pointer
#                 return node #return current node
#             output = reverseFirstN(node.next, nxt_ptr, n-1) # get the following node
#             node.next.next = node
#             node.next = nxt_ptr[0] # point self next to the saved following node
#             return output
#         if left == 1:
#             return reverseFirstN(head, nxt_ptr, right)
#         else: #keep going to the range where left becomes the first node.
#             head.next = self.reverseBetween(head.next, left-1, right-1)
#             return head


# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         nxt = [None]
#         def reverseN(node, nxt, n): #to reverse the first N
#             if n == 1:
#                 nxt[0] = node.next
#                 return node
#             output = reverseN(node.next, nxt, n-1)
#             node.next.next = node
#             node.next = nxt[0]
#             return output
#
#         if left == 1:
#             return reverseN(head, nxt, right)
#         head.next = self.reverseBetween(head.next, left-1, right-1) #go into the reverseN, and it will become reverse first N case, with ongoing left-1.
#         return head







# previous approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         prev = None
#         root = head
#         pos = 0
#         while head: #keep going until the reverse part
#             pos += 1
#             if pos == left:
#                 arr = [head.val]
#                 while pos < right:
#                     head = head.next
#                     arr.append(head.val)
#                     pos += 1
#                 rev_start = ListNode(arr.pop()) # reverse
#                 rev_node = rev_start
#                 while arr:
#                     rev_node.next = ListNode(arr.pop())
#                     rev_node = rev_node.next
#                 rev_node.next = head.next #the following part is the rest of the linked list
#                 if prev == None: #put the reverse part with the rest
#                     return rev_start
#                 else:
#                     prev.next = rev_start
#                     return root
#             else:
#                 prev = head
#                 head = head.next





# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if head == None: return None
#         node = head
#         i = 1
#         temp = []
#         start = None
#         while node:
#             if m <= i <= n:
#                 temp.append(node)
#                 if i == n:
#                     while temp:
#                         t = temp.pop()
#                         if start == None:
#                             start = ListNode(t.val)
#                             o_node = start
#                         else:
#                             o_node.next = ListNode(t.val)
#                             o_node = o_node.next
#             else:
#                 if start == None:
#                     start = ListNode(node.val)
#                     o_node = start
#                 else:
#                     o_node.next = ListNode(node.val)
#                     o_node = o_node.next
#             node = node.next
#             i+=1
#         return start



