# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: 'ListNode', a: int, b: int, list2: 'ListNode') -> 'ListNode':
        output = node = list1
        cnt = 0
        while node:
            prev = node
            node = node.next
            cnt += 1
            if cnt == a:
                prev.next = list2
                tail_list2 = list2
                while tail_list2.next:
                    tail_list2 = tail_list2.next
            elif cnt == b + 1:
                tail_list2.next = node

        return output

