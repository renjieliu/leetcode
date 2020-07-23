"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def helper(output, node):
            if node.children == []:
                return 0
            else:
                curr = [0] * len(node.children)
                for i, c in enumerate(node.children):
                    curr[i] = 1 + helper(output, c)

                downLevels = curr[0]
                for i in range(
                        len(curr) - 1):  # check the level for each children, add it with another, to get the local max
                    for j in range(i + 1, len(curr)):
                        downLevels = max(downLevels, curr[i] + curr[j])
                output[0] = max(output[0], downLevels)
                return max(curr)

        if root == None:
            return 0
        else:
            output = [0]
            helper(output, root)
            return output[0]
