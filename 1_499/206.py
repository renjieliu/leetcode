# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def flat(node, lst):
            while node:
                lst.append(node.val)
                node = node.next

        if head == None:
            return None
        else:
            lst = []
            flat(head, lst)
            output = ListNode(lst.pop())
            node = output
            while lst:
                node.next = ListNode(lst.pop())
                node = node.next
            return output

# Below is the recursive approach

#         def flat(node,lst):
#             if node:
#                 lst.append(node.val)
#                 flat(node.next, lst)
#         if head== None :return None
#         else:
#             lst = []
#             flat(head, lst)
#             output = ListNode(lst.pop())
#             node = output
#             while lst:
#                 node.next = ListNode(lst.pop())
#                 node = node.next
#             return output
