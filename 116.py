"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root == None: return root

        def flat(node, idx, lvl):
            if idx != 2 ** lvl - 2:  # no node on the right
                node.next = findNext(idx + 1, root, 0)
            if node.left:
                flat(node.left, idx * 2 + 1, lvl + 1)
            if node.right:
                flat(node.right, idx * 2 + 2, lvl + 1)

        def findNext(target, node, idx):
            if idx == target:
                return node
            else:
                if node.left:
                    ans = findNext(target, node.left, 2 * idx + 1)
                    if ans:
                        return ans
                if node.right:
                    ans = findNext(target, node.right, 2 * idx + 2)
                    if ans:
                        return ans

        flat(root, 0, 1)
        return root


















