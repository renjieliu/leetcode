# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> 'List[TreeNode]':
        if N % 2 == 0: return None
        dp = {0: [None], 1: [TreeNode(0)]}  # to find all the possible shape for each count of the node
        for total in range(3, N + 1, 2):
            dp[total] = []
            for L in range(0, total):
                R = total - 1 - L  # -1 is for the root node
                if L in dp and R in dp:
                    for x in dp[L]:
                        for y in dp[R]:
                            dp[total].append(TreeNode(0, x, y))

        return dp[N]

