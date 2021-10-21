# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]': #O(N)
        neg = [] #put the negative number
        pos = [] #put the positive number
        while head: #flat the linked list
            if head.val < 0:
                neg.append(head.val)
            else: 
                pos.append(head.val)
            head = head.next
        
        output = None
        node = None

        if neg: #starting from negative number
            output = ListNode(neg.pop())
            node = output
            while neg:
                node.next = ListNode(neg.pop()) 
                node = node.next 
    
        if pos: #add the positive numbers to the negative list
            pos = pos[::-1]
            
            if output == None: #initialize node, if no neg numbers.
                output = ListNode(pos.pop())
                node = output
            
            while pos:
                node.next = ListNode(pos.pop())
                node = node.next 
                
        return output
                

            
            
            