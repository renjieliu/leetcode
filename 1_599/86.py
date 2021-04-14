# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None: return None
        arr_1 = []
        arr_2 = []
        while head:
            if head.val < x:
                arr_1.append(head.val)
            else:
                arr_2.append(head.val)
            head = head.next
        if arr_1:
            start = ListNode(arr_1.pop(0))
        else:
            start = ListNode(arr_2.pop(0))
        node = start
        for a in arr_1 + arr_2:
            node.next = ListNode(a)
            node = node.next
        return start


    # previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def partition(self, head: ListNode, x: int) -> ListNode:
#         if head == None: return None
#         flat = []
#         while head:
#             flat.append(head.val)
#             head = head.next
#         left = []
#         right = []
#         while flat:
#             if flat[0] < x:
#                 left.append(flat.pop(0))
#             else:
#                 right.append(flat.pop(0))
#         pool = left + right
#         start = ListNode(pool.pop(0))
#         node = start
#         while pool:
#             node.next = ListNode(pool.pop(0))
#             node = node.next
#         return start
