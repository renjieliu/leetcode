# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: 'Optional[ListNode]') -> 'List[int]':
        arr = []
        prev = None
        i = 0
        while head:
            if prev and head.next:
                if (head.val > prev and head.val > head.next.val) or (head.val < prev and head.val < head.next.val):
                    arr.append(i)
            prev = head.val 
            i+=1
            head = head.next
        output = [float('inf'), -float('inf')]
        if len(arr) < 2:
            return [-1, -1]
        
        for i, a in enumerate(arr): #for each number, check distance with neighbors for the minn , and head/tail for the maxx
            if i == 0 :
                output[0] = min(output[0], abs(a-arr[i+1]))
                output[1] = max(output[1], abs(a-arr[-1]) )
            elif i == len(arr)-1:
                output[0] = min(output[0], abs(a-arr[i-1]))
                output[1] = max(output[1], abs(a-arr[0]) )
            else:
                output[0] = min(output[0], min(abs(a-arr[i-1]), abs(a-arr[i+1]) ))
                output[1] = max(output[1], max(abs(a-arr[-1]), abs(a-arr[0]) ))
            
        return output
                    
                    



