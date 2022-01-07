# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: 'Optional[ListNode]'):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        loc = random.randint(0, len(self.arr)-1)
        return self.arr[loc]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

 

# previous approach 

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# import random


# class Solution:

#     def __init__(self, head: 'ListNode'):
#         """
#         @param head The linked list's head.
#         Note that the head is guaranteed to be not null, so it contains at least one node.
#         """
#         self.arr = []
#         while head:
#             self.arr.append(head.val)
#             head = head.next

#     def getRandom(self) -> int:
#         """
#         Returns a random node's value.
#         """
#         return self.arr[random.randint(0, len(self.arr) - 1)]

# # Your Solution object will be instantiated and called as such:
# # obj = Solution(head)
# # param_1 = obj.getRandom()