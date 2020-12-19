# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> 'List[List[int]]':
        if root == None: return []

        def helper(batch, node, root):
            if node.left == node.right == None:
                batch[0].append(node.val)
                return 0
            else:
                L = R = -float('inf')
                if node.left:
                    L = helper(batch, node.left, root) + 1
                if node.right:
                    R = helper(batch, node.right, root) + 1
                currBatch = max(L, R)  # the batch number for the current node to be removed
                if currBatch not in batch:
                    batch[currBatch] = []
                if node != root:
                    batch[currBatch].append(node.val)
                return currBatch

        batch = {0: []}
        helper(batch, root, root)
        if len(batch) == 1:
            return [batch[k] for k in sorted(list(batch.keys())) if batch[k]]
        return [batch[k] for k in sorted(list(batch.keys())) if batch[k]] + [
            [root.val]]  # the final batch is the root, and root is excluded from the helper function




















