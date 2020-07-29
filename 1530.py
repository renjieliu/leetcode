# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node, level, distance, output):
            if node.left == node.right == None:
                return [level]
            else:
                left_down = []
                right_down = []
                if node.left:
                    left_down = dfs(node.left, level + 1, distance, output)
                if node.right:
                    right_down = dfs(node.right, level + 1, distance, output)

                if len(left_down + right_down) > 1:  # from left to right leaf, see if the path length <= distance
                    for i in range(len(left_down)):
                        currLeft = left_down[i] - level  # the true level going down
                        for j in range(len(right_down)):
                            currRight = right_down[j] - level
                            if currLeft + currRight <= distance:
                                output[0] += 1

                return left_down + right_down

        output = [0]
        dfs(root, 0, distance, output)
        return output[0]


