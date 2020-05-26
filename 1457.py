# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def isPalin(arr):  # at most, 1 odd occurrence can happen, otherwise, it cannot be a palindrome
            hmp = {}
            for a in arr:
                if a not in hmp:
                    hmp[a] = 0
                hmp[a] += 1
            odd = 0
            for v in hmp.values():
                if v % 2 != 0:
                    odd += 1
            return 1 if odd < 2 else 0

        def flat(node, curr, output):
            if node.left == node.right == None:
                output[0] += isPalin(curr + [node.val])
            else:
                if node.left:
                    flat(node.left, curr + [node.val], output)
                if node.right:
                    flat(node.right, curr + [node.val], output)

        if root == None: return 0
        output = [0]
        flat(root, [], output)
        return output[0]
