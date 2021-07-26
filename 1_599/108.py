# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> TreeNode:
        def helper(arr):
            if arr:
                mid = len(arr)//2
                node = TreeNode(arr[mid])
                node.left = helper(arr[:mid]) #build left with left half of the arr
                node.right = helper(arr[mid+1:])#build right with right half of the arr
                return node
        return helper(nums)

