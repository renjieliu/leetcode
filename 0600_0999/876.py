# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]': # O( N | 1 )
        def helper(output, node, idx): 
            if node.next == None:
                if idx == (idx+1) // 2: #idx is total // 2. Since current node is the last one, the total is idx+1
                    output[0] = node 
                return idx+1 # total nodes in the list
            else: 
                total = helper(output, node.next, idx+1)
                if idx == total // 2:
                    output[0] = node 
                return total
        
        output = [None]
        helper(output, head, 0)
        return output[0]





# previous solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        output = [None] 
        def helper(output, node, level): #check how many levels in total, and if current level is total//2+1 (the middle node)
            if node.next:
                total = helper(output, node.next, level+1) 
            else:
                total = level
            if level == total//2+1:
                output[0] = node 
            
            return total
        
        helper(output, head, 1)
        return output[0]
            
                


# previous approach
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         def flat(stk, node):
#             if node.next == None:
#                 stk.append(node)
#             else:
#                 stk.append(node)
#                 flat(stk, node.next)
#         stk = []
#         flat(stk, head)
#         return stk[len(stk)//2]


