# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> 'List[int]':
        def flat(node, output):
            if node.left == node.right == None:
                if node.val not in output:
                    output[node.val] = 0
                output[node.val] += 1
            else:
                if node.val not in output:
                    output[node.val] = 0
                output[node.val] += 1
                if node.left != None:
                    flat(node.left, output)
                if node.right != None:
                    flat(node.right, output)
        ans = []
        if root == None:
            return ans
        else:
            output = {}
            flat(root, output)
            find = max(output.values())
            for k , v in output.items():
                if v == find:
                    ans.append(k)
            return ans