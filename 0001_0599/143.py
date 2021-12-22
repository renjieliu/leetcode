# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: 'Optional[ListNode]') -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def helper(arr, node, level, total): # using dfs to replace in place
            arr.append(node.val)
            if node.next:
                helper(arr, node.next, level+1, total)
                if level <= (total[0] +1)//2: #only work on the first half
                    N = ListNode(arr[-level])
                    N.next = node.next
                    node.next = N 
                
                if level == (total[0] +1)//2: #remove the second half
                    if total[0] % 2 == 1:
                        node.next = None 
                    elif node.next:
                        node.next.next = None
            else:
                total[0] = level
        total = [0]
        helper([], head, 1, total)
        #print(total)
            
            
                
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if head: #generate a new linked list, and copy the new list to head
#             node = head 
#             arr = []
#             while node:
#                 arr.append(node.val)
#                 node = node.next
            
#             root = ListNode(arr.pop(0))
#             node = root
#             i = 1
#             while arr:
#                 if i % 2 == 1:
#                     node.next = ListNode(arr.pop())
#                 else:
#                     node.next = ListNode(arr.pop(0))
#                 node = node.next 
#                 i += 1 
            
#             root = root.next
#             node = head
#             node.next = root
#             while root:
#                 node.next = root 
#                 node = node.next
#                 root = root.next
            
            
            
            
            
                 



# previous approach

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if head ==None: return None
#         node = head
#         stk = []
#         while node:
#             stk.append(node.val)
#             node = node.next
#         node = head #preserve the head node
#         stk.pop(0)
#         turn = 1
#         while stk:
#             node.next = ListNode(stk.pop(-turn))
#             turn = abs(turn-1) #1 to 0, 0 to 1
#             node = node.next