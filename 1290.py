# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stk = []
        output = 0 
        while head!=None:
            stk.append(head.val)
            head = head.next
        
        p=0
        for i in stk[::-1]:
            output+= (2**p)*i
            p+=1
        return output
        