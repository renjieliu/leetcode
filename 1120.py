# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def dfs(output, node):
            if node.left == node.right == None:
                output[0] = max(output[0], node.val)
                return [node.val, 1] #[sum, count]
            else:
                t_left = [0,0] #[sum from left subtree, count from left subtree]
                t_right = [0,0] #[sum from right subtree, count from right subtree]

                if node.left:
                    t_left = dfs(output, node.left)
                if node.right:
                    t_right = dfs(output, node.right)

                output[0] = max(output[0],  (t_left[0] + t_right[0] + node.val) / (1+t_left[1] + t_right[1]))
                return [node.val + t_left[0] + t_right[0], t_left[1] + t_right[1] + 1]

        output = [-float('inf')]
        dfs(output, root)
        return output[0]



