# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def flat(stk, node):
            if node.next == None:
                stk.append(node)
            else:
                stk.append(node)
                flat(stk, node.next)
        stk = []
        flat(stk, head)
        return stk[len(stk)//2]