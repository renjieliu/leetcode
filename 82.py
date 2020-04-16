# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        else:
            node = head
            curr = node.val
            cnt = 0
            start_node = None
            while node:
                pre = curr
                curr = node.val
                if curr == pre:
                    cnt += 1
                else:
                    if cnt == 1:
                        if start_node == None:
                            start_node = ListNode(pre)
                            follow_node = start_node
                        else:
                            follow_node.next = ListNode(pre)
                            follow_node = follow_node.next
                        cnt = 1
                    else:
                        cnt = 1
                node = node.next

            if cnt == 1:  # for the last node, to see if it's dups
                if start_node == None:
                    start_node = ListNode(curr)
                    follow_node = start_node
                else:
                    follow_node.next = ListNode(curr)
                    follow_node = follow_node.next

            return start_node