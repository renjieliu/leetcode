# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        prev = None
        root = head
        pos = 0
        while head: #keep going until the reverse part
            pos += 1
            if pos == left:
                arr = [head.val]
                while pos < right:
                    head = head.next
                    arr.append(head.val)
                    pos += 1
                rev_start = ListNode(arr.pop()) # reverse
                rev_node = rev_start
                while arr:
                    rev_node.next = ListNode(arr.pop())
                    rev_node = rev_node.next
                rev_node.next = head.next #the following part is the rest of the linked list
                if prev == None: #put the reverse part with the rest
                    return rev_start
                else:
                    prev.next = rev_start
                    return root
            else:
                prev = head
                head = head.next





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



