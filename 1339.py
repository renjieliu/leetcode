# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: 'Optional[TreeNode]') -> int:
        mod = 10**9+7
        def total(s, idx, dp, node):
            if node.left == node.right == None:
                s[0] += node.val
                dp[idx] = [0,0] #left subtree, right subtree
                return node.val
            else:
                s[0] += node.val
                left = right = 0
                if node.left:
                    left = total(s, idx*2+1, dp, node.left)
                if node.right:
                    right = total(s, idx*2+2, dp, node.right)
                dp[idx] = [left, right]
                return node.val + left + right

        s = [0] #total sum in the tree
        dp = {} #to record left sub and right sub sum of the node
        total(s, 0, dp, root)

        def compare(output, s, idx, dp, node):
            if node.left: #assuming take out the left edge
                left = dp[idx][0]
                output[0] = max(output[0], left * (s[0] - left)) #left sub * all the remaining
                compare(output, s, idx*2+1, dp, node.left)
            if node.right: #assuming take out the right edge
                right = dp[idx][1]
                output[0] = max(output[0], right * (s[0] - right)) #right sub * all the remaining
                compare(output, s, idx*2+2, dp, node.right)

        output = [-float('inf')]
        compare(output, s, 0, dp, root)
        return output[0] % mod

