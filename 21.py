# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            output = ListNode(l1.val if l1.val <= l2.val else l2.val)
            if output.val == l1.val:
                l1 = l1.next
            else:
                l2 = l2.next
            node = output
            while l1 or l2:
                if l1 == None:
                    node.next = ListNode(l2.val)
                    l2 = l2.next
                elif l2 == None:
                    node.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    if l1.val <= l2.val:
                        node.next = ListNode(l1.val)
                        l1 = l1.next
                    else:
                        node.next = ListNode(l2.val)
                        l2 = l2.next
                node = node.next
            return output



