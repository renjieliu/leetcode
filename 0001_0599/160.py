# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: 'ListNode', headB: 'ListNode') -> 'Optional[ListNode]': # O(M+N | 1)
        nodeA = headA
        nodeB = headB        
        while nodeA != nodeB: #to make both nodes to start at the same length, and compare each node.
            nodeA = headB if nodeA == None else nodeA.next  
            nodeB = headA if nodeB == None else nodeB.next
        return nodeA



# previous solution

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: 'ListNode', headB: 'ListNode') -> Optional['ListNode']: # O(M+N | N)
#         lkp = set() # store each node of A
        
#         while headA:
#             lkp.add(headA)
#             headA = headA.next
        
#         while headB: 
#             if headB in lkp: # if current node is in A, intersection is found
#                 return headB
#             headB = headB.next
#         return None

    
# previous solution

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         nodeA = headA
#         nodeB = headB
#         while nodeA!=nodeB:
#             nodeA = headB if nodeA == None else nodeA.next
#             nodeB = headA if nodeB == None else nodeB.next
#         return nodeA




# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         A = 0 #count how many nodes in A
#         B = 0 #count how many nodes in B
#         nodeA = headA
#         nodeB = headB
#         prevA = headA
#         prevB = headB
#
#         while headA:
#             A += 1
#             prevA = headA
#             headA = headA.next
#
#         while headB:
#             B += 1
#             prevB = headB
#             headB = headB.next
#
#         if prevA != prevB: # last element is not the same, so no overlapping
#             return None
#
#         while nodeA and A > B: # make both same length
#             nodeA = nodeA.next
#             A-=1
#
#         while nodeB and  B > A: # make both same length
#             nodeB = nodeB.next
#             B-=1
#
#         while nodeA and nodeB: # keep moving both until meet the common element
#             if nodeA != nodeB:
#                 nodeA = nodeA.next
#                 nodeB = nodeB.next
#             else:
#                 return nodeA
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
