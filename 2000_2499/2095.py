# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        def helper(before, node, prevNode): # to find how many nodes are after here
            if node.next == None:
                total = before + 1 
                if before == total // 2: #this is the middle node
                    if prevNode:
                        prevNode.next = node.next
                    else: #this is the first node, and it needs to be deleted
                        return None
                return 1
            
            else:
                after = helper(before+1, node.next, node)
                total = before+1+after 
                if before == total//2: #this is the middle node
                    if prevNode: 
                        prevNode.next = node.next
                return after+1
                
        T = helper(0, head, None)
        return head if T else None
                
                        
                
            
        