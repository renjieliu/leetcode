
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(nxt, node): #nxt: the next node of the last child node pointing to
            if node.child == node.next == None: 
                node.next = nxt
                if nxt:
                    nxt.prev = node #doubly linked,  the prev of next node should be the last child node
            elif node.child:
                N = node.next # save the next node 
                node.next = node.child # point the next to child 
                node.child.prev = node # point the prev of child to current node
                helper(N if N else nxt, node.child) #go to child , and flatten
                node.child = None #remove the child node, as it has become the next node.
                if N:
                    helper(nxt, N) #proceed to next node
                
            elif node.next:
                helper(nxt, node.next)
            
            return node
            
        if head == None:
            return head
        
        return helper(None, head)



# previous approach
# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
# """

# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         def dfs(node, output):
#             if node.child == node.next == None:
#                 output.append(node.val)
#             else:
#                 output.append(node.val)
#                 if node.child:
#                     dfs(node.child, output)
#                 if node.next:
#                     dfs(node.next, output)

#         if head == None :return None
#         else:
#             output = []
#             dfs(head, output)
#             if len(output) == 1:
#                 return Node(output[0], None, None, None)
#             start = Node(output[0], None , None)
#             old = start
#             node = start.next
#             output.pop(0) #take out the first node
#             while output: #Node(val, prev, next, child)
#                 node = Node(output[0], old, None, None) #prev node would be the old node
#                 old.next = node
#                 old = node
#                 node = node.next #make next as the curr node
#                 output.pop(0)
#             return start


