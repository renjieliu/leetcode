# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> 'List[int]':
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        output = []
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                output.append(arr[i + 1])
            else:
                output.append(-1)
        output.append(0)  # add 0 for the last element

        stk = []
        for i in range(len(output) - 2, -1, -1):  # find the closest in the stack, which is larger,  if cannot find a larger, use 0, and push current number to the stack
            if output[i] != -1:  # pretend current number is a larger number
                stk.append(output[i])
            else:
                while stk:
                    if stk[-1] > arr[i]:
                        output[i] = stk[-1]
                        stk.append(arr[i])
                        break
                    stk.pop()
                if output[i] == -1:
                    output[i] = 0
                    stk.append(arr[i])
        return output




