# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        def helper(node):
            if node.next == None:
                return node
            res = helper(node.next)
            node.next.next = node
            node.next = None
            return res
        return helper(head) if head else None



# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         def flat(node, lst):
#             while node:
#                 lst.append(node.val)
#                 node = node.next
#
#         if head == None:
#             return None
#         else:
#             lst = []
#             flat(head, lst)
#             output = ListNode(lst.pop())
#             node = output
#             while lst:
#                 node.next = ListNode(lst.pop())
#                 node = node.next
#             return output
#
# # Below is the recursive approach
#
# #         def flat(node,lst):
# #             if node:
# #                 lst.append(node.val)
# #                 flat(node.next, lst)
# #         if head== None :return None
# #         else:
# #             lst = []
# #             flat(head, lst)
# #             output = ListNode(lst.pop())
# #             node = output
# #             while lst:
# #                 node.next = ListNode(lst.pop())
# #                 node = node.next
# #             return output
