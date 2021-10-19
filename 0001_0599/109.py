# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        def helper(arr):
            if len(arr) == 0 :
                return None
            else:
                s = len(arr)//2
                currNode = ListNode(arr[s])
                currNode.left = helper(arr[:s])
                currNode.right = helper(arr[s+1:])
                return currNode
        node = helper(arr)
        return node


