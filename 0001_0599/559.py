"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int: #BFS approach
        if root == None:
            return 0
        else:
            level = 0
            stk = [root]
            while stk:
                nxt = []
                level+=1
                while stk:
                    node = stk.pop()
                    for c in node.children:
                        nxt.append(c)
                stk = nxt
            return level
        


