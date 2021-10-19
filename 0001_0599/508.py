# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> 'List[int]':
        if root == None: return []

        def flat(output, node, dp, index):
            if index in dp:
                return dp[index]
            else:
                if node.left == node.right == None:
                    dp[index] = node.val
                else:
                    A = B = 0
                    S = node.val
                    if node.left:
                        A = flat(output, node.left, dp, 2 * index + 1)
                    if node.right:
                        B = flat(output, node.right, dp, 2 * index + 2)
                    dp[index] = A + B + S

                if dp[index] not in output:
                    output[dp[index]] = 0
                output[dp[index]] += 1
                return dp[index]

        output = {}
        dp = {}
        flat(output, root, dp, 0)
        occ = max(output.values())
        res = []
        for k, v in output.items():
            if v == occ:
                res.append(k)
        return res



