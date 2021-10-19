# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def helper(node, n):
            if node == None:
                return [0, None]  # [layer 0, None]
            else:
                layer_nodes = helper(node.next, n)
                if -(layer_nodes[
                         0] + 1) == -n:  # if current layer is the layer n from end, then return the nodes below it.
                    return [layer_nodes[0] + 1, layer_nodes[1]]
                else:
                    curr = ListNode(node.val)  # else, add the current node to the return chain
                    curr.next = layer_nodes[1]
                    return [layer_nodes[0] + 1, curr]

        return helper(head, n)[1]

# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         if n == 1 :
#             arr = arr[:-n]
#         else:
#             arr = arr[:-n] + arr[-n+1:]
#         if arr == []:
#             return None
#         s = ListNode(arr.pop(0))
#         node = s
#         while arr:
#             node.next = ListNode(arr.pop(0))
#             node = node.next
#         return s