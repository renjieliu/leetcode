# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: 'ListNode') -> int:
        def helper(output, node): #one pass DFS to calc the output
            if node.next == None:
                output[0] += node.val
                return 0
            else:
                level = helper(output, node.next) + 1
                output[0] += node.val * (2**level)
                return level
        
        output = [0]
        helper(output, head)
        return output[0]

    

# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         curr = ""
#         while head:
#             curr+=str(head.val)
#             head = head.next
#         return int(curr,2)