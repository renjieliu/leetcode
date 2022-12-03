# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]': # O( N | N )
        arr = []
        while head: # flat the list
            arr.append(head.val)
            head = head.next
        
        curr = arr[-1]
        i = len(arr)-2 
        while i > -1: # find if there's no nodes larger than current node
            if arr[i] < curr: # mark the ones to be removed as -1 
                arr[i] = None
            elif arr[i] > curr:
                curr = arr[i]
            i -= 1

        while arr: # initialize the new node
            if arr[0] == None: 
                arr.pop(0)
            else:
                break
        
        newRoot = ListNode(arr.pop(0))
        curr = newRoot
        while arr:
            if arr[0] != None: 
                curr.next = ListNode(arr[0])
                curr = curr.next
            arr.pop(0)
        
        return newRoot

    
            
        
