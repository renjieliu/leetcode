# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: 'Optional[ListNode]') -> bool: # O( N | N )
        arr = []
        while head: # flat and compare
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]
    


# previous solution

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         return arr == arr[::-1]