# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: 'List[Optional[ListNode]]') -> 'Optional[ListNode]':
        def flat(arr, node):
            while node: 
                arr.append(node.val)
                node = node.next
        
        arr = []
        for node in lists: # flat each node, sort, and generate the new ListNode.
            flat(arr, node)
        arr.sort(reverse = True)
        if arr == []:
            return None
        else:
            start = ListNode(arr.pop())
            node = start
            while arr:
                node.next = ListNode(arr.pop())
                node = node.next
            return start



# previous approach

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
#         flat = []
#         for l in lists:
#             while l:
#                 flat.append(l.val)
#                 l = l.next
#         flat.sort()
#         if len(flat) == 0: return None
#         start = ListNode(flat.pop(0))
#         node = start
#         while flat:
#             node.next = ListNode(flat.pop(0))
#             node = node.next
#         return start

