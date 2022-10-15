# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]': # O( N | 1 )
        def helper(node, idx): # current node, current index, starting from 0 
            if node.next == None:
                return [idx, None if idx == (idx+1)//2 else node]  #idx+1 is the total length 
            
            total, nxt = helper(node.next, idx+1)
            if idx == (total+1) // 2:
                return [total, nxt]
            node.next = nxt
            return [total, node]
            
        return helper(head, 0)[1]
                
                

# previous solution

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteMiddle(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
#         def helper(before, node, prevNode): # to find how many nodes are after here
#             if node.next == None:
#                 total = before + 1 
#                 if before == total // 2: #this is the middle node
#                     if prevNode:
#                         prevNode.next = node.next
#                     else: #this is the first node, and it needs to be deleted
#                         return None
#                 return 1
            
#             else:
#                 after = helper(before+1, node.next, node)
#                 total = before+1+after 
#                 if before == total//2: #this is the middle node
#                     if prevNode: 
#                         prevNode.next = node.next
#                 return after+1
                
#         T = helper(0, head, None)
#         return head if T else None
                
                        
                
            
        