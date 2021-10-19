# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: 'Optional[ListNode]', k: int) -> 'List[Optional[ListNode]]':
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)

        if k > n:
            output = []
            while arr:
                output += [ListNode(arr.pop(0))]

            output += [None for _ in range(k-n)]
            return output

        else:
            output = []
            while arr:
                start = ListNode(arr.pop(0))
                curr = start
                cnt = 1
                target = n // k + (1 if len(output) < n%k else 0)
                while cnt < target and arr:
                    curr.next = ListNode(arr.pop(0))
                    curr = curr.next
                    cnt +=1
                output += [start]
            return output





# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def splitListToParts(self, root: ListNode, k: int) -> 'List[ListNode]':
#         flat = []
#         while root:
#             flat.append(root.val)
#             root = root.next
#         if k > len(flat):
#             arr = [[_] for _ in flat] + [[] for i in range(k - len(flat))]
#         else:
#             rem = len(flat) % k  # first rem will have one more element than the rest
#             cnt = len(flat) // k  # each arr will have cnt elements
#             arr = [[]]
#             while flat:
#                 if len(arr[-1]) < cnt + (1 if len(arr) <= rem else 0):
#                     arr[-1].append(flat.pop(0))
#                 else:
#                     arr.append([flat.pop(0)])
#
#         def buildListNode(arr):
#             if arr == []:
#                 return None
#             root = ListNode(arr[0])
#             node = root
#             for a in arr[1:]:
#                 node.next = ListNode(a)
#                 node = node.next
#             return root
#
#         return [buildListNode(_) for _ in arr]
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
