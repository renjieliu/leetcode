# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: 'Optional[ListNode]') -> int:
        def helper(output, arr, node):
            if node.next ==None:
                output[0] = max(output[0], node.val + arr.pop(0)) #compare the tail with the head (twin nodes)
            else:
                arr.append(node.val)
                helper(output, arr, node.next)
                if arr:
                    output[0] = max(output[0], node.val + arr.pop(0)) #compare curr with curr head (twin nodes)
        output = [-float('inf')]
        helper(output, [], head)
        return output[0]

    
