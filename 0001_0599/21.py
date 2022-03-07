# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: 'Optional[ListNode]', list2: 'Optional[ListNode]') -> 'Optional[ListNode]':
        start = ListNode() #dummy start node, return start.next
        node = start 
        while list1 and list2: #check every node, and put the smaller one here
            if list1.val<=list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2 #put the rest of list1 or list2
        return start.next
    
    


# previous approach

# # Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 == None: return l2
#         if l2 == None: return l1

#         if l1.val <= l2.val:
#             start = ListNode(l1.val)
#             l1 = l1.next
#         else:
#             start = ListNode(l2.val)
#             l2 = l2.next

#         node = start
#         while l1 and l2:
#             if l1.val<=l2.val:
#                 node.next = ListNode(l1.val)
#                 node = node.next
#                 l1 = l1.next
#             else:
#                 node.next = ListNode(l2.val)
#                 node = node.next
#                 l2 = l2.next

#         node.next = l1 if l1 else l2
#         return start















