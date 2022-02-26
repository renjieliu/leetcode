# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        def findMid(node):
            slow = fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None  #cut the linked nodes in half.
            return mid
        
        def merge(A, B): #merge sort, go through each node of the 2 lists, and linked the current smaller one to the prev node.
            if A==None or B == None:
                return A or B
            else:
                if A.val <= B.val:
                    start = A 
                    node = start 
                    A = A.next
                else:
                    start = B
                    node = B
                    B = B.next 
                while A and B:
                    if A.val <= B.val:
                        node.next = A
                        A = A.next 
                    else:
                        node.next = B
                        B = B.next
                    node = node.next
                node.next = A or B # add the rest of A or B to the node
                return start
        
        if head == None or head.next == None:
            return head
        mid = findMid(head)
        L = self.sortList(head)
        R = self.sortList(mid)
        
        return merge(L,R)
                
                    
                    


# previous approach

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
#         def findMid(node): #using fast and slow pointer to find the mid
#             fast = slow = node
#             while fast.next and fast.next.next:
#                 fast = fast.next.next
#                 slow = slow.next 
            
#             mid = slow.next 
#             slow.next = None # cut the list into half
#             return mid
               
#         def merge(A, B): #merge 2 nodes, just like merging 2 arrays, keep checking each number at the front
#             if A == None or B == None:
#                 return A or B
#             else:
#                 if A.val <= B.val:
#                     start = A
#                     node = start
#                     A = A.next
#                 else: 
#                     start = B 
#                     node = start
#                     B = B.next
#                 while A and B:
#                     if A.val <= B.val: 
#                         node.next = A 
#                         A = A.next
#                         node = node.next
#                     else:
#                         node.next = B
#                         B = B.next
#                         node = node.next
                
#                 node.next = A or B #take the rest of A or B                         

#             return start
        
        
#         if head == None or head.next == None :
#             return head 
#         else: 
#             mid = findMid(head) 
#             L = self.sortList(head) # sort the first half
#             R = self.sortList(mid) # sort the second half
             
#             return merge(L, R) # merge the first and second half
        

        
        
        
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         arr = []
#         while head: # just flat, sort, and form a new ListNode
#             arr.append(head.val)
#             head = head.next
#         arr.sort()
#         root = ListNode(arr[0])
#         node = root
#         for i in range(1, len(arr)):
#             node.next = ListNode(arr[i])
#             node = node.next
#         return root





# previous approach

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         def flat(output, node):
#             while node:
#                 output.append(node.val)
#                 node = node.next

#         output = []
#         flat(output, head)
#         output.sort()
#         if output == []:
#             return None
#         start = ListNode(output.pop(0))
#         node = start
#         while output:
#             node.next = ListNode(output.pop(0))
#             node = node.next
#         return start
