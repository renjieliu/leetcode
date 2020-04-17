# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None: return None
        node = head
        i = 1
        temp = []
        start = None
        while node:
            if m <= i <= n:
                temp.append(node)
                if i == n:
                    while temp:
                        t = temp.pop()
                        if start == None:
                            start = ListNode(t.val)
                            o_node = start
                        else:
                            o_node.next = ListNode(t.val)
                            o_node = o_node.next
            else:
                if start == None:
                    start = ListNode(node.val)
                    o_node = start
                else:
                    o_node.next = ListNode(node.val)
                    o_node = o_node.next
            node = node.next
            i+=1
        return start