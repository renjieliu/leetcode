# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]': # O( N | 1 )
        if head == None:
            return None
        odd = head # assign the head to odd
        even = head.next # head.next is even
        firstEven = head.next # this is the first even to return
        
        while even and even.next: #iterate with the even pointer
            odd.next = even.next # assign the even next to odd next
            odd = odd.next # move the odd pointer 
            
            even.next = odd.next # assign the odd next to even 
            even = even.next # move the even pointer 
        odd.next = firstEven  # merge oddList with evenList
    
        return head

        




# previous solution

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution: # O(N) + O(1) space
#     def oddEvenList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
#         if head == None:
#             return None 
#         start = head #the return start
#         prevOdd = head  #previous odd
#         prevEven = None #previous even 
#         firstEven = None #first Even. the most recent found odd node need to point to this one as next 
#         i = 1 
#         head = head.next 
#         while head:
#             i += 1
#             if i % 2: 
#                 t = head.next #save the curent next pointer
#                 prevOdd.next = head
#                 prevEven.next = head.next #point the prevEven to next
#                 head.next = firstEven # move curr odd the last odd sequence, and point to the first Even
#                 prevOdd = head
#                 head = t
#             else:
#                 if firstEven == None: #save the first even
#                     firstEven = head
#                 prevEven = head  #save current node as prevEven
#                 head = head.next # move to the next 
                
#         return start
                
            
                


# previous approach :O(N) + O(N) space
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if head == None: return None
#         even = []
#         odd = []
#         p = 0
#         while head:
#             if p % 2 == 0:
#                 even.append(head.val)
#             else:
#                 odd.append(head.val)
#             head = head.next
#             p += 1
#         head = ListNode(even.pop(0))
#         node = head
#         while even:
#             node.next = ListNode(even.pop(0))
#             node = node.next
#         while odd:
#             node.next = ListNode(odd.pop(0))
#             node = node.next
#         return head

