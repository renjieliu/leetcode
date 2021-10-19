# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = l1.val+l2.val
        l1 = l1.next
        l2 = l2.next
        carry = 0 if curr < 10 else 1
        curr = curr % 10
        root = ListNode(curr)
        node = root
        while l1 and l2:
            curr = l1.val+l2.val + carry
            carry = 0 if curr < 10 else 1
            curr = curr % 10
            node.next = ListNode(curr)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr = l1.val+carry
            carry = 0 if curr < 10 else 1
            curr = curr % 10
            node.next = ListNode(curr)
            node = node.next
            l1 = l1.next
        while l2:
            curr = l2.val+carry
            carry = 0 if curr < 10 else 1
            curr = curr % 10
            node.next = ListNode(curr)
            node = node.next
            l2 = l2.next

        if carry == 1: # the final digit. for case as 9+2, the 1 need to be appended after iteration
            node.next = ListNode(1)
            node = node.next

        return root






# previous approach
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         #calculate to an array, and build the ListNode from the array
#         #In order to build the ListNode, need to initialize the head, then add the body
#         #Do not initiate the next node for the last node.
#         carry  = 0
#         stk_1 = []
#         stk_2 = []
#         while l1:
#             stk_1.append(l1.val)
#             l1=l1.next
#         while l2:
#             stk_2.append(l2.val)
#             l2=l2.next
#         short = stk_1 if len(stk_1) <= len(stk_2) else stk_2
#         long = stk_2 if short == stk_1 else stk_1
#         res = []
#         while short:
#             t = short.pop(0)+long.pop(0)+ carry
#             carry = 1 if t >= 10 else 0
#             res.append( t- (10 if carry ==1 else 0))
#         while long: #add the remaining to the res stk
#             t = long.pop(0)+ carry
#             carry = 1 if t >= 10 else 0
#             res.append( t- (10 if carry ==1 else 0))
#
#         if carry ==1:
#             res.append(1)
#
#         output = ListNode(0) #Head
#         tmp = output # body
#         for i in range(len(res)):
#             tmp.val = res[i]
#             if i < len(res)-1 :
#                 tmp.next = ListNode(0)
#                 tmp = tmp.next
#         return output
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#