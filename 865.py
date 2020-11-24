# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def flat(output, node, curr):
            if node.left == node.right == None:
                output.append(curr + [node.val])
            else:
                if node.left: flat(output, node.left, curr + [node.val])
                if node.right: flat(output, node.right, curr + [node.val])

        output = []
        flat(output, root, [])
        layer = max(map(lambda x: len(x), output))
        arr = [_ for _ in output if len(_) == layer]
        if len(arr) == 1:  # only one deepest node
            v = arr[-1][-1]
        else:
            v = arr[0][0]  # find the common ancestor
            loop = 1
            commonPath = []
            while loop == 1:
                cnt = 0
                base = arr[0][0]
                for a in arr:
                    if a.pop(0) == base:  # the head value should be same for all the path
                        cnt += 1
                if cnt == len(arr):
                    v = base
                else:
                    loop = 0

        def find(target, ans, node):
            if node.val == target:
                ans.append(node)
            else:
                if node.left:
                    find(target, ans, node.left)
                if node.right:
                    find(target, ans, node.right)

        ans = []
        find(v, ans, root)
        return ans[0]




























