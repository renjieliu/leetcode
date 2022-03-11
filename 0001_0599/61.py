# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: 'Optional[ListNode]', k: int) -> 'Optional[ListNode]':
        def helper(output, lvl, oldhead, node, k):
            if node.next == None: # reach the end of the list
                fromBottom = 1
                total = lvl
                if k % total != 0: #if k%total != 0 , the end of the listnode will connect to the old head
                    node.next = oldhead
            else:
                t = helper(output, lvl+1, oldhead, node.next, k)
                total = t[0]
                fromBottom = t[1]+1 
            
            if k % total == fromBottom:
                output[0] = node
            
            elif k % total == fromBottom - 1:
                node.next = None #next node is new head, set current.next to None, to avoid cycle.

            return [total, fromBottom] # total nodes, levels from bottom
        
        if head == None:
            return head
        output = [None]
        helper(output, 1, head, head, k)
        
        return output[0] or head #if output[0] is none ==> total % k == 0, then just return the head.

    
    

    


# previous approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if head == None:
#             return None
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         realRotate = k % len(arr)
#         for i in range(realRotate):
#             arr = [arr[-1]] + arr[:-1]
#         start = ListNode(arr.pop(0))
#         output = start
#         while arr:
#             output.next = ListNode(arr.pop(0))
#             output = output.next
#         return start
            

# previous approach

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if k == 0:
#             return head
#         else:
#             stk = []
#             while head != None:
#                 stk.append(head.val)
#                 head = head.next
#             if stk == []:
#                 return None
#             else:
#                 k = k % len(stk)
#                 arr = stk[-k:].copy() + stk[:-k].copy()
#                 output = ListNode(arr[0])
#                 arr.pop(0)
#                 node = output
#             while arr:
#                 node.next = ListNode(arr.pop(0))
#                 node = node.next
#             return output





