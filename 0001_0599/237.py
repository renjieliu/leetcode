# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node): # O( N | 1 )
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next: # exist next node
            node.val = node.next.val #mode next node val to current node 
            if node.next.next: # if the next node is not the last node
                node = node.next
            else: # next node is the last node, trim it, and return the result
                node.next = None 



# previous solution

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
#         node.val = node.next.val
#         node.next = node.next.next

