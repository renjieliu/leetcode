# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> TreeNode:
        def maxPos(arr):
            if len(arr) == 1:
                return 0
            else:
                ma = -float('inf')
                output = -1
                for i, n in enumerate(arr):
                    if n > ma:
                        ma = n
                        output = i
                return output

        def buildTree(arr, pivot, tree):
            if len(arr) == 0:
                return None
            else:
                leftMaxPos = maxPos(
                    arr[:pivot])  # find the max pos in the left part, and make that pos as the root to iterate left
                rightMaxPos = maxPos(arr[
                                     pivot + 1:])  # find the max pos in the right part, and make that pos as the root to iterate right
                if leftMaxPos != -1:
                    tree.left = TreeNode(arr[:pivot][leftMaxPos])
                    buildTree(arr[:pivot], leftMaxPos, tree.left)  # left
                if rightMaxPos != -1:
                    tree.right = TreeNode(arr[pivot + 1:][rightMaxPos])
                    buildTree(arr[pivot + 1:], rightMaxPos, tree.right)  # right

        pivot = maxPos(nums)
        tree = TreeNode(nums[pivot])
        buildTree(nums, pivot, tree)
        return tree






















